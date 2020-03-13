from django.shortcuts import render
<<<<<<< HEAD
import io
=======
>>>>>>> c1c4e66e205e315f215949c57a6f3a7444012473
import json
# Create your views here.

def menu(request):
<<<<<<< HEAD
    data = []
    file = io.open(r"C:\Users\Денис\PycharmProjects\fitrisa_toy\fetrisa_toy_app\data.txt", "r", encoding='utf-8')
    file_data = []
    for row in file:
        file_data.append(row.replace("\n", "").split("; "))
    print(file_data)
    x =[]
    for i in range(0, len(file_data)):
        x.append(file_data[i][1])
    x.sort(reverse=True)
    for i in range(0, len(x)):
        c = file_data.index(x[i])
        data.append(file_data[c])
        file_data.pop(c)
    return render(request, '1.htm', {"data": data})
=======
    so = {}
    for i in range(10):
        so[i] = i+10
    so = json.dumps(so)
    return render(request, '1.htm', {'data': so})
>>>>>>> c1c4e66e205e315f215949c57a6f3a7444012473

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

