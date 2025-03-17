from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def gestion_scolarite(request): 
    return render(request, 'gestion_scolarite.html')