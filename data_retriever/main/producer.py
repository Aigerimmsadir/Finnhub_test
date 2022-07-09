import json , pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit_mq'))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='companies', body=body, properties=properties)

