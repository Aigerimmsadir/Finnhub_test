import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_sender.settings")

app = Celery("email_sender")
app.conf.enable_utc = False
app.conf.update(timezone=os.environ.get('local_tz'))
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(['main', ])