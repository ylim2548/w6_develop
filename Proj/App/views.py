from django.shortcuts import render
from .models import Teammate

# Create your views here.

def home(request):
    Teammates = Teammate.objects.all()
    return render(request, 'home.html', {'Teammate':Teammates})