import json
from django.core.mail import send_mail
from email_server.email_sender.settings import EMAIL_HOST_USER


def compute_news(rsstr):
    news = json.loads(rsstr)
    sorted_by_tickets = {

    }
    for companynew in news:
        sorted_by_tickets[companynew['related']] = sorted_by_tickets[
            companynew['related']] if companynew['related'] in sorted_by_tickets else []
        sorted_by_tickets[companynew['related']].append(companynew)
    print(sorted_by_tickets)
    send_mail(
        json.dumps(sorted_by_tickets),
        'Here is the message.',
        EMAIL_HOST_USER,
        ['aigerimsadir@gmail.com'],
        fail_silently=False,
    )
