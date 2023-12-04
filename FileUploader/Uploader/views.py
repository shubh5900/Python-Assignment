from django.shortcuts import render

# Create your views here.

def FileUploader(request):
    return render(request,"uploader.html")