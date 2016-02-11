from django.core.mail import send_mail

def sendemail(name, email, message):
    send_mail('Inquiry', message, email, ['chyungspice@gmail.com'])
