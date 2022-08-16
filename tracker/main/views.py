from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Application
from .forms import AddApplication

def index(response):
    return render(response, "main/index.html", {})


def create(response):
    if response.method == "POST":
        form = AddApplication(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
           
        return render(response)
