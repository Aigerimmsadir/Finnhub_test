import imp
from celery import shared_task
import requests
import json
from .models import CompanyNew, TicketInterest
from datetime import datetime, timedelta
import pytz
from django.core.mail import send_mail
from email_sender.settings import EMAIL_HOST_USER

@shared_task(name="send_daily")
def send_daily():
    print('started')
    today = datetime.now().replace(hour=0, minute=0,second=0,microsecond=0)
    CompanyNew.objects.filter(datetime_created__lt=today).delete()
    
    tickets = list(TicketInterest.objects.exclude(users_subscribed=None).prefetch_related('users_subscribed'))
    group_by_tickets={

    }
    news=list(CompanyNew.objects.all())
    for nnew in news:
        if nnew.related in tickets:
            group_by_tickets[nnew.related]=group_by_tickets[nnew.related] if nnew.related in group_by_tickets else []
            group_by_tickets[nnew.related].append(nnew.summary)
    for gt in group_by_tickets:
        users_subscr = list(gt.users_subscribed.all())
        emails = [us.email for us in users_subscr]
        content =group_by_tickets[gt]
        send_mail(
            json.dumps(content[:5]),
            'Summary',
            EMAIL_HOST_USER,
            emails,
            fail_silently=False,
        )
