from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request, "index.html")


def mail(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        to = request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [to,]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("done")



