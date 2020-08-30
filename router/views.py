from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Route
from .forms import RouterForm
# Create your views here.

def home(request):
    # return HttpResponse('Site is working')
    form = RouterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"URL has been successfully shortened to {request.get_raw_uri()}{form.cleaned_data.get('key')}")
        return redirect('home')
    return render(request, 'router/home.html', {"form": form})

def redirector(request, key):

    instance = get_object_or_404(Route, key= key)
    return redirect(instance.original_url)