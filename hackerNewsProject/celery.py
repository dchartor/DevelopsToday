import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackerNewsProject.settings")

app = Celery("hackerNewsProject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
