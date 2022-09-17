import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("DailyCodeApp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.CELERY_BEAT_SCHEDULE = {
    'update_profiles_from_leetcode_api': {
        'task': 'src.tasks.user.update_profiles_from_leetcode_api',
        'schedule': crontab(),
    },
}
