from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Route
from .forms import RouterForm
# Create your views here.

def home(request):
    # return HttpResponse('Site is working')
    form = RouterForm(request.POST or None)
    return render(request, 'router/home.html', {"form": form})

def redirector(request, key):

    # if key == "000001":
    #     return redirect("https://www.youtube.com/watch?v=qmxoGYCFruM")
    instance = get_object_or_404(Route, key= key)
    return redirect(instance.original_url)