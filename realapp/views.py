from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    housings = Housing.objects.all()[0:4]
    return render(request, 'index.html',{"housings":housings})


def rooms(request, pk):
    housings = Housing.objects.filter(pk=pk)
    return render(request, 'rooms.html',{"housings":housings})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def property(request):
    housings =  Housing.objects.all()
    context = {
        "housings":
        housings
    }
    return render(request, 'prop.html', context)
