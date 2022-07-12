import json
from django.core.mail import send_mail
from email_sender.settings import EMAIL_HOST_USER
from main.models import TicketInterest

def compute_news(rsstr):
    news = json.loads(rsstr)
    sorted_by_tickets = {

    }
    for companynew in news:
        sorted_by_tickets[companynew['related']] = sorted_by_tickets[
            companynew['related']] if companynew['related'] in sorted_by_tickets else []
        sorted_by_tickets[companynew['related']].append(companynew)
    print(sorted_by_tickets)
    for t in sorted_by_tickets:
        ticket = TicketInterest.objects.get_or_create(name=t['related'])
        subscribers =list( t.users_subscribed.all())
        if subscribers:
            emails = [s.email for s in subscribers]
            send_mail(
                json.dumps(sorted_by_tickets),
                'TicketNew',
                EMAIL_HOST_USER,
                emails,
                fail_silently=False,
            )
