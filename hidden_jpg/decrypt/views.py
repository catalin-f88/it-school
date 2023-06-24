from django.shortcuts import render
from django.http import HttpResponse  
from stegano import exifHeader

# Create your views here.
def decrypt(request):
    try:
        if request.method == 'POST' and request.FILES['file']:  
            uploaded_file = request.FILES['file']
            decoded_message = str(exifHeader.reveal(uploaded_file))
            return render(request,"result.html", {'result':decoded_message[1:]})
    except Exception as err:
        return render(request, "decrypt.html", {"error": err})
    else:  
        return render(request,"decrypt.html")