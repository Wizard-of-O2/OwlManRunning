import os
import subprocess
import pika
import json
from oci.config import from_file
from oci.object_storage import ObjectStorageClient
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv("../.env")

oci_config = from_file()
oci_namespace = "cnqwgzok7slt"
oci_bucket = "bucket-1"

upload_path = os.environ["UPLOAD_PATH"]

queue_name = "omr"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["AMQP_HOST"], heartbeat=120))
channel = connection.channel()

client = MongoClient(os.environ["MONGODB_URL"])
db = client.test

channel.queue_declare(queue=queue_name, durable=True)
channel.basic_qos(prefetch_count=1)


def upload_oci(path, count):
    client = ObjectStorageClient(oci_config)
    
    # TODO: drop first

    for i in range(1, count+1):
        with open(f"{upload_path}/{path}/result/result_{i}.png", "rb") as f:
            client.put_object(oci_namespace, oci_bucket, f"{path}/result_{i}.png", f,
                              content_type="image/png")

def callback(ch, method, properties, body):
    print("[x] Received %r" % body.decode())

    a = db.scores.find_one({"_id": ObjectId(body.decode())})
    ans = None
    if a["answer"] != None:
        # save answer to json file
        ans = db.answers.find_one({"_id": a["answer"]})
        del ans["_id"]
        ans_path = f"{upload_path}/{a['path']}/answer.json"
        with open(ans_path, "w") as f:
            json.dump(ans, f)
    
    # run omr_processor
    print("[x] Start processing")

    params = ["python", "omr_reader/main.py", f"{upload_path}/{a['path']}/{a['filename']}", a["type"]]
    if ans:
        params.insert(2, "-a")
        params.insert(3, f"{upload_path}/{a['path']}/answer.json")

    p = subprocess.run(params, capture_output=True)
    if p.returncode == 0:
        # update to database
        r = json.loads(p.stdout)
        db.scores.update_one({"_id": a["_id"]}, {"$set": {"status": "finish", "result": r}})

        # upload file to OCI
        upload_oci(a['path'], len(a["result"]))
    else:
        print(p.stderr)
        db.scores.update_one({"_id": a["_id"]}, {"$set": {"status": "error"}})

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("[x] Finish processing")

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("[x] worker started.")
channel.start_consuming()
