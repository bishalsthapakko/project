from django.shortcuts import render, HttpResponse

# views.py
from django.shortcuts import render
from .models import Storeinstruments

def home(request):
    images = Storeinstruments.objects.all().order_by('-created_at')
    context = {
        'images': images
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def instruments(request):
    return render(request, 'instruments.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
