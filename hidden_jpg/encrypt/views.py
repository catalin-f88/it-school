from django.shortcuts import render
from django.http import HttpResponse  
from encrypt.forms import UserForm
from stegano import exifHeader
import mimetypes
import os
import pathlib

   
def encrypt(request):  
    if request.method == 'POST':  
        user = UserForm(request.POST, request.FILES)  
        if user.is_valid():  
            output_file = 'encrypt/upload/'+"encrypted_" + request.FILES['file'].name
            # if pathlib.Path(output_file).suffix != ".jpeg" or pathlib.Path(output_file).suffix != ".jpg":
            #     user = UserForm()
            #     return render(request, "encrypt.html", {"form": user, "error": "[ERROR] The file you uploaded is not a valid .JPG image! \n Please upload a .JPG file bellow:"})
            exifHeader.hide(request.FILES['file'], output_file, request.POST['message'])
            model_instance = user.save(commit=False)
            model_instance.save()
            path = open(output_file, 'rb')
            mime_type, _ = mimetypes.guess_type(output_file)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % output_file
            return response
    else:  
        user = UserForm()  
        return render(request,"encrypt.html",{'form':user, 'error': ""})