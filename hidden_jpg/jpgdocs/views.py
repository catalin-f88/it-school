from django.shortcuts import render
from encrypt.models import UserForm

# Create your views here.
def docs(request):
    counter = UserForm.objects.filter().count()
    return render(request,"docs.html",{'counter':counter})