from django.shortcuts import render
from django.http import HttpResponse  
from stegano import exifHeader

# Create your views here.
def decrypt(request):
    """ Using stegano module, an encrypted hidden message inside a .JPG file is decrypted and returned to user.
    In order to work properly, the functions needs a .jpg or .jpeg file (no other image formats supported)
    that contains an encrypted message.
    If the file is not a .jpeg or .jpg or does not contain a message, the user will receive an 
    error message parsed to the user in the {{ error }} variable.
    If the decryption succeeds, result.html is returned to the user with the resulted message shown 
    inside the {{ result }}.
    """
    try:
        if request.method == 'POST' and request.FILES['file']:  
            uploaded_file = request.FILES['file']
            decoded_message = str(exifHeader.reveal(uploaded_file))
            return render(request,"result.html", {'result':decoded_message[1:]})
    except Exception as err:
        return render(request, "decrypt.html", {"error": err})
    else:  
        return render(request,"decrypt.html")