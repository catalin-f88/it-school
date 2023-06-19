from django.shortcuts import render
from django.http import HttpResponse  
from encrypt.forms import UserForm
from stegano import exifHeader
import mimetypes
import os

   
def encrypt(request):  
    if request.method == 'POST':  
        user = UserForm(request.POST, request.FILES)  
        if user.is_valid():  
            output_file = 'encrypt/upload/'+"encrypted_" + request.FILES['file'].name
            exifHeader.hide(request.FILES['file'], output_file, request.POST['message'])
            model_instance = user.save(commit=False)
            model_instance.save()
            if output_file != '':
                path = open(output_file, 'rb')
                mime_type, _ = mimetypes.guess_type(output_file)
                response = HttpResponse(path, content_type=mime_type)
                response['Content-Disposition'] = "attachment; filename=%s" % output_file
                return response
            else:
                return HttpResponse("Error processing your file.")

    else:  
        user = UserForm()  
        return render(request,"encrypt.html",{'form':user})