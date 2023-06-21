from django.shortcuts import render
from encrypt.models import UserForm
from django.http import HttpResponse 

# Create your views here.
def home(request):
    counter = UserForm.objects.filter().count()
    return render(request,"home.html",{'counter':counter})