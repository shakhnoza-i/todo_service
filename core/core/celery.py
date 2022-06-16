from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core') # core - project name
app.conf.enable_utc = False # cause we use our own timezone
app.conf.update(timezone = 'Asia/Almaty')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)