from django.shortcuts import render
from website import mail

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        message = request.POST['message']
        mail.sendemail(name, email, message)
        return render(request, 'website/contact_success.html')

    else:
        return render(request, 'website/contact.html')
