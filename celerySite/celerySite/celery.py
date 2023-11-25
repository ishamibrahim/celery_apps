from celery import Celery
from celery.schedules import crontab
import os

os.environ['DJANGO_SETTINGS_MODULE'] = "celerySite.settings"
app = Celery('celerySite', broker='redis://localhost:6379/0')


app.conf.result_backend = 'redis://localhost:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run_square-ten-seconds': {
        # Task Name (Name Specified in Decorator)
        'task': 'celeryApp.tasks.check_square',
        # Schedule
        'schedule': 10.0
    },
}

@app.task(bind=True)
def hello(self):
    return 'hello world'
