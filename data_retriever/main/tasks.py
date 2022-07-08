from celery import shared_task
import requests


@shared_task(name="obtain_companies_finnhub")
def obtain_companies_finnhub():
    print('yes')
    res = requests.get(
        'https://finnhub.io/api/v1/company-news?token=cb36h0aad3i3uh8votcg&symbol=AAPL&from=2022-01-11&to=2022-07-07',
    )
    print(res.text)
