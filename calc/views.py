from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Add Two Numbers'})

def add(request):

    val1 = int(request.POST['extra7'])
    val2 = int(request.POST['extra8'])
    res = val1 + val2

    return render(request, 'result.html', {'result':res})
