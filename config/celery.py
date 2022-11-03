import os
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam_every_5_minute': {
        'task': 'src.manager.tasks.send_beat_email',
        'schedule': crontab(minute='*/2')
    }
}
