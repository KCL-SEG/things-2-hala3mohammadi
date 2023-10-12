from django.shortcuts import render
from .forms import ThingForm 

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    form = ThingForm()
    return render(request, 'sign_up.html', {'form': form})