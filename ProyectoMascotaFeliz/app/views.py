from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')

def somos(request):
    return render (request, 'somos.html')

def register(request):
    return render (request, 'register.html')

def galeria(request):
    return render (request, 'galeria.html')

def feriados(request):
    return render (request, 'feriados.html')



    


