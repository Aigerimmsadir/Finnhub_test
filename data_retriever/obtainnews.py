from sys import path
from os import environ
import django
path.append('/workspace/data_retriever/data_retriever/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_retriever.settings')


django.setup()

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def obtain_news():
    print('here')
    # IntervalSchedule.objects.all().delete()
    schedule, newsch = IntervalSchedule.objects.get_or_create(
        every=15,
        period=IntervalSchedule.SECONDS,
    )
    
    task_name = 'obtain_news_finnhub'
    PeriodicTask.objects.filter(name=task_name).delete()
    # periodic task that will send emails everyday
    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task='obtain_news_finnhub',

    )
    print('started')

obtain_news()