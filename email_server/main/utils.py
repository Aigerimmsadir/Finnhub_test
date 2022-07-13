import json
from django.core.mail import send_mail
from email_sender.settings import EMAIL_HOST_USER
from main.models import TicketInterest, CompanyNew

def compute_news(rsstr):
    news = json.loads(rsstr)
    sorted_by_tickets = {

    }
    companynew_obs = []
    tickets_by_name = {}
    for companynew in news:
        sorted_by_tickets[companynew['related']] = sorted_by_tickets[
            companynew['related']] if companynew['related'] in sorted_by_tickets else []
        sorted_by_tickets[companynew['related']].append(companynew)
        ticket = TicketInterest.objects.get_or_create(name=companynew['related'])[0]
        tickets_by_name[companynew['related']] = ticket
        companynew = CompanyNew(
                datetime_created=companynew['datetime_created'],
                headline=companynew['headline'],
                unique_id=str(companynew['unique_id']),
                image=companynew['image'],
                related=ticket,
                source=companynew['source'],
                summary=companynew['summary'],
                url=companynew['url']
            )
        companynew_obs.append(companynew)
    CompanyNew.objects.bulk_create(companynew_obs)
    print(sorted_by_tickets)
    for t in sorted_by_tickets:
        ticket = tickets_by_name[t]
        subscribers =list( ticket.users_subscribed.all())
        if subscribers:
            emails = [s.email for s in subscribers]
            send_mail(
                json.dumps(sorted_by_tickets),
                'TicketNew',
                EMAIL_HOST_USER,
                emails,
                fail_silently=False,
            )


    print("newscreated",CompanyNew.objects.count())
