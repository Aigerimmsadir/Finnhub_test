from django.http import HttpResponse
from .tasks import *
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule


# Create your views here.
def current_datetime(request):
    print('here', request)
    IntervalSchedule.objects.all().delete()
    schedule, newsch = IntervalSchedule.objects.get_or_create(
        every=7,
        period=IntervalSchedule.SECONDS,
    )
    task_name = 'obtain_companies_finnhub'
    # periodic task that will send emails everyday
    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task='obtain_companies_finnhub',

    )
    return HttpResponse(status=201)
