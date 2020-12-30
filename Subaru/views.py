from django.shortcuts import render
from .models import Models

# Create your views here.
def index(request):
    models = Models.objects.all()
    return render(request,'index.html',{'models':models})