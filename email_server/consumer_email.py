
import pika
import json
import django
from sys import path
from os import environ
import pytz

# Your path to settings.py file
path.append('/workspace/email_server/email_sender/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')

django.setup()
from main.utils import compute_news
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit_mq', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='newstickets')


def callback(ch, method, properties, body):
    print("Received ...", properties.content_type, body)
    local_tz = pytz.timezone("Asia/Almaty")
    try:
        data = json.loads(body)
    except Exception as e:
        print(e)

    if properties.content_type == 'news_added':
        compute_news(body)



channel.basic_consume(
    queue='newstickets', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
