from django.shortcuts import render
from encrypt.models import UserForm
from django.http import HttpResponse 

# Create your views here.
def home(request):
    """ Redirects the user to home.html and shows counter of usage. """
    counter = UserForm.objects.filter().count()
    return render(request,"home.html",{'counter':counter})