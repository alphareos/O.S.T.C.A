from django.shortcuts import render
from django.core.mail import send_mail
from .models import Clients

# Create your views here.
def home(request):
    clients = Clients.objects.all()
    return render(request, 'index.html', {'clients': clients})
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        message_name = request.POST['subject']
        message_email = request.POST['email']
        #message_subject = request.POST['subject']
        message = request.POST['message']

        #send email
        send_mail(
            message_name,#message name
            #message_subject,#message subject
            message, #message
            message_email,#from email
            ['muleta822@gmail.com'], #to email

        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html')

def testimonials(request):
    return render(request, 'testimonials.html')
def services(request):
    return render(request, 'services.html')
