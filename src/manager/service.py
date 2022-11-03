from django.core.mail import send_mail


def send():
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем присылать вам много спама',
        'ermakoventer777@gmail.com',
        ['ermakoventer777@gmail.com'],
        fail_silently=False,
    )