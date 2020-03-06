from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, '1.htm')

def toys(request):
    return render(request, '2.html')

def sets(requesr):
    return render(requesr, '3.html')

def stocks(requesr):
    return render(requesr, '4.html')

def process(requesr):
    return render(requesr, '5.html')

def ets(requesr):
    return render(requesr, '6.html')