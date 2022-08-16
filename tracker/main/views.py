from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ApplicationList, Application
from .forms import AddApplication

def index(response):
    return render(response, "main/index.html", {})


def create(response):
    if response.method == "POST":
        form = AddApplication(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            a = ApplicationList(name=n)
            a.save()
        return render(response)
