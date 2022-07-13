
import pika
import json
import django
from sys import path
from os import environ
from datetime import datetime
import pytz


# Your path to settings.py file
path.append('/workspace/finnhub_main/finnhub_main/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'finnhub_main.settings')

django.setup()
from main.models import CompanyNew
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit_mq', heartbeat=0))
channel = connection.channel()
channel.queue_declare(queue='companies')
from main.producer import publish

def callback(ch, method, properties, body):
    print("Received ...")
    local_tz = pytz.timezone("Asia/Almaty")
    try:
        data = json.loads(body)
    except Exception as e:
        print(e)

    if properties.content_type == 'company_added':
        print('yes')
        companies_new = data
        companynew_objs = []
        companynew_objs_json = []
        for cn in companies_new:
            timestamp_date = cn['datetime']
            utc_dt = datetime.utcfromtimestamp(
                timestamp_date).replace(tzinfo=pytz.utc)
            local_dt = local_tz.normalize(utc_dt.astimezone(local_tz))

            companynew = CompanyNew(
                datetime_created=local_dt,
                headline=cn['headline'][:500],
                unique_id=str(cn['id']),
                image=cn['image'][:500],
                related=cn['related'][:500],
                source=cn['source'][:500],
                summary=cn['summary'][:500],
                url=cn['url'][:500]
            )
            companynew_objs_json.append({
                'datetime_created':local_dt.strftime('%Y-%m-%dT%H:%M:%S%z'),
                'headline':cn['headline'][:500],
                'unique_id':str(cn['id']),
                'image':cn['image'][:500],
                'related':cn['related'][:500],
                'source':cn['source'][:500],
                'summary':cn['summary'][:500],
                'url':cn['url'][:500]
            })
            companynew_objs.append(companynew)

        CompanyNew.objects.bulk_create(companynew_objs)
        print(CompanyNew.objects.count())
        publish('news_added', json.dumps(companynew_objs_json))


channel.basic_consume(
    queue='companies', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
