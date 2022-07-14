from sys import path
from os import environ
import django
path.append('/workspace/email_server/email_sender/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_sender.settings')

django.setup()

from django_celery_beat.models import PeriodicTask, IntervalSchedule

def daily_sum_send():
    print('here')
    # IntervalSchedule.objects.all().delete()
    schedule, newsch = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS,
    )
    task_name = 'send_daily'
    PeriodicTask.objects.filter(name=task_name).delete()
    # periodic task that will send emails everyday
    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task='send_daily',

    )
    print('sent')


daily_sum_send()
