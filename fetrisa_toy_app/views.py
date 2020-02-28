from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, '1.htm')

def toys(request):
    return render(request, '2.html')