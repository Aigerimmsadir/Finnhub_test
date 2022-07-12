import json , pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit_mq', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='companies', body=body, properties=properties)

