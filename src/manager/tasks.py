from config.celery import app
from src.manager.service import send


@app.task
def send_beat_email():
    send()