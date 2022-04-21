from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def attractions(request):
    return render(request, 'attractions.html', {})

def funfacts(request):
    return render(request, 'funfacts.html', {})