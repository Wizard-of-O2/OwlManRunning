import os
import pika
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

    # update to database
    db.scores.update_one({'_id': ObjectId(body.decode())}, 
        {'$set': {'status': 'finish'}})

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name, on_message_callback=callback)
channel.start_consuming()
