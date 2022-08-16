from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Application
from .forms import AddApplication

def home(response):
    application = Application.objects.all()
    context = {
        'application': application
         } 
       
 
    return render(response, "main/home.html", context)


def add(response):
    if response.method == "POST":
        form = AddApplication(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
           
    return render(response, "main/add.html", {})
