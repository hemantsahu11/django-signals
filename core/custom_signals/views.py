from django.shortcuts import render
from django.http import HttpResponse
from .signals import notification
# Create your views here.


def home(request):
    # sending signals from views
    notification.send(sender=None, request=request, user=['Hemant', 'Amritesh'])
    return HttpResponse("Home page custom signals ")
