from django.shortcuts import render
from encrypt.models import UserForm

# Create your views here.
def docs(request):
    """ Redirects the user to docs.html and shows counter of usage. """
    counter = UserForm.objects.filter().count()
    return render(request,"docs.html",{'counter':counter})