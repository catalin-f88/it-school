from django.shortcuts import render
from django.http import HttpResponse
from encrypt.forms import UserForm
from stegano import exifHeader
import mimetypes
import os


def encrypt(request):
    """ Using stegano module, encrypt a hidden message inside a .JPG file.
    In order to work properly, the functions needs the following:
    - a .jpg or .jpeg file (no other image formats supported)
    - a short message to be encrypted
    After the message is embedded in the image, a new file with the hidden message will be returned
    to the user. The message can only be decrypted if this image is parsed to the decrypt() function.
    """
    if request.method == 'POST':
        user = UserForm(request.POST, request.FILES)
        if user.is_valid():
            output_file = 'encrypt/upload/' + \
                "encrypted_" + request.FILES['file'].name
            ext = os.path.splitext(output_file)[-1].lower()
            if ext == ".jpg" or ext == ".jpeg":
                exifHeader.hide(
                    request.FILES['file'], output_file, request.POST['message'])
                model_instance = user.save(commit=False)
                model_instance.save()
                path = open(output_file, 'rb')
                mime_type, _ = mimetypes.guess_type(output_file)
                response = HttpResponse(path, content_type=mime_type)
                response['Content-Disposition'] = "attachment; filename=%s" % output_file
                return response
            else:
                user = UserForm()
                return render(request, "encrypt.html", {"form": user, "error": "[ERROR] The file you uploaded is not a valid .JPG image! \n Please upload a .JPG file bellow:"})
        return render("encrypt.html", {"form": user, "error": "Message encrypted. The hidden message is hidden in the downloaded image!"})
    else:
        user = UserForm()
        return render(request, "encrypt.html", {'form': user, 'error': ""})
