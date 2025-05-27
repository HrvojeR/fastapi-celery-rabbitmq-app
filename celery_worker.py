from celery import Celery
from celery.schedules import crontab
from settings import RABBITMQ_URL
from datetime import timedelta

celery_app = Celery(
    'celery_worker',
    broker=RABBITMQ_URL,
    backend="rpc://",  # RPC backend za RabbitMQ (ili zadrži REDIS_URL ako želiš Redis za rezultate)
    include=["tasks"]
)

celery_app.conf.beat_schedule = {
    'print-random-item-every-1-seconds': {
        'task': 'tasks.insert_random_item',
        'schedule': timedelta(seconds=1),
    },
}

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Sarajevo",
    enable_utc=True,
)
