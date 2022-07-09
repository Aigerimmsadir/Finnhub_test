import imp
from celery import shared_task
import requests
from .producer import publish
import json
from .models import CompanyNew
from datetime import datetime, timedelta
import pytz


@shared_task(name="obtain_news_finnhub")
def obtain_news_finnhub():
    print('yes')
    datetime_now = datetime.now().replace(hour=0, microsecond=0, minute=0, second=0)
    today_date = datetime_now
    tomorrow_date = datetime_now+timedelta(days=1)
    today_str = today_date.strftime('%Y-%m-%d')
    tomorrow_str = tomorrow_date.strftime('%Y-%m-%d')
    news = []
    res = requests.get(
        f'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=TSLA&newfrom={today_str}&to={tomorrow_str}',
    )
    news_tsla = json.loads(res.text)
    news.extend(news_tsla)
    res = requests.get(
        f'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=FB&newfrom={today_str}&to={tomorrow_str}',
    )
    news_fb = json.loads(res.text)
    news.extend(news_fb)
    res = requests.get(
        f'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=AMZN&newfrom={today_str}&to={tomorrow_str}',
    )
    news_amzn = json.loads(res.text)
    news.extend(news_amzn)
    res = requests.get(
        f'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=TWTR&newfrom={today_str}&to={tomorrow_str}',
    )
    news_twtr = json.loads(res.text)
    news.extend(news_twtr)
    res = requests.get(
        f'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=+3&newfrom={today_str}&to={tomorrow_str}',
    )
    news_nflx = json.loads(res.text)
    news.extend(news_nflx)
    news_set = []
    news_set_ids = []
    for n in news:
        if n['id'] not in news_set_ids:
            news_set.append(n)
            news_set_ids.append(n['id'])
    news_existing = list(CompanyNew.objects.filter(
        datetime_created__gte=today_date))
    companies_new = [n for n in news_set if str(
        n['id']) not in [ne.unique_id for ne in news_existing]]

    local_tz = pytz.timezone("Asia/Almaty")

    if companies_new:
        companynew_objs = []
        for cn in companies_new:
            timestamp_date = cn['datetime']
            utc_dt = datetime.utcfromtimestamp(
                timestamp_date).replace(tzinfo=pytz.utc)
            local_dt = local_tz.normalize(utc_dt.astimezone(local_tz))

            company = CompanyNew(
                datetime_created=local_dt,
                headline=cn['headline'][:500],
                unique_id=str(cn['id']),
                image=cn['image'][:500],
                related=cn['related'][:500],
                source=cn['source'][:500],
                summary=cn['summary'][:500],
                url=cn['url'][:500]
            )
            companynew_objs.append(company)
        CompanyNew.objects.bulk_create(companynew_objs)
        print(CompanyNew.objects.count())
        publish('company_added', json.dumps(companies_new))
