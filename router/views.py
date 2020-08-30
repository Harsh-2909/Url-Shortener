from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Site is working')

def redirector(request, key):
    if key == "000001":
        return redirect("https://www.youtube.com/watch?v=qmxoGYCFruM")