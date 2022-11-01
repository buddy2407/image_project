from django.shortcuts import render,redirect
from .models import Images
from django.core.files.storage import FileSystemStorage

# Create your views here.
def Home(request):
    image = Images.objects.all().order_by('-id')
    return render(request,'home.html',{'image':image})
def save_image(request):
    if request.method == "POST":
        img=Images()
        img.image_name=request.POST.get('image_name')
        img.image=request.FILES['image']
        # fs=FileSystemStorage()
        img.save()
    return redirect('home')