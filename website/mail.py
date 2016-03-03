from django.core.mail import send_mail

def sendemail(name, email, message):
    send_mail('Inquiry', 'Message from: ' + email + ' ' + message + ' -- auto generated from Absolute Design Website', email, ['contact@absolutedesigncompany.com'])
