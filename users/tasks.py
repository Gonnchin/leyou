from celery import task
from django.core.mail import send_mail


@task
def email_regiester(mailbox, content):
    print('----send')
    send_mail(subject='乐游网注册',
              message=content,
              from_email='Python__test@163.com',
              recipient_list=[mailbox],)
    print('----end')