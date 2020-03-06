from django.shortcuts import render
import io

# Create your views here.

def menu(request):
    data = {}
    file = io.open(r"C:\Users\Денис\PycharmProjects\fitrisa_toy\fetrisa_toy_app\data.txt", "r", encoding='utf-8')
    file_data = []
    for row in file:
        file_data.append(row.replace("\n", "").split("; "))
    print(file_data)
    for i in range(0, len(file_data)):
        data[str(i)] = file_data[i]
    return render(request, '1.htm', {"data": data})

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