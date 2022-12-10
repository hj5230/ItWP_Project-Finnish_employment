from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def employ(request):
    return render(request, 'employ.html')

def pension(request):
    return render(request, 'pension.html')