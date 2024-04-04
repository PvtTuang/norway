from django.shortcuts import render
from .models import Image

# Create your views here.

def image_list(request):
    return render(request, 'norway/image_list.html')