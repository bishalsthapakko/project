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


# views.py
def instruments(request):
    instruments = Storeinstruments.objects.all().order_by('-created_at')
    context = {
        'instruments': instruments
    }
    return render(request, 'instruments.html', context)


def contact(request):
    return render(request, 'contact.html')

# Create your views here.
