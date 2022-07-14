import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_retriever.settings")

app = Celery("data_retriever")
app.conf.enable_utc = False

app.conf.update(timezone=os.environ.get('local_tz'))
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(['main', ])
