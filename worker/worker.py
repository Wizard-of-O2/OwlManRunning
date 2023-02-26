import os
import subprocess
import pika
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

queue_name = 'omr'
connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['AMQP_HOST']))
channel = connection.channel()

client = MongoClient(os.environ['MONGODB_URL'])
db = client.test

channel.queue_declare(queue=queue_name, durable=True)
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print("[x] Received %r" % body.decode())

    a = db.scores.find_one({"_id": ObjectId(body.decode())})
    
    # run omr_processor
    print("[x] Start processing")
    p = subprocess.run(["python", "omr_reader/main.py", f"../{a['path']}", a["type"]], capture_output=True)
    if p.returncode == 0:
        # update to database
        r = json.loads(p.stdout)
        db.scores.update_one({"_id": a["_id"]}, {"$set": {"status": "finish", "result": r}})
    else:
        db.scores.update_one({"_id": a["_id"]}, {"$set": {"status": "error"}})

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("[x] Finish processing")

channel.basic_consume(queue=queue_name, on_message_callback=callback)
channel.start_consuming()
