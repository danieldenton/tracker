from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Application
from .forms import AddApplication

def home(response):
    app = Application.objects.get()
    context = {
        "company": app.company,
        "job_title": app.job_title,
        "date_listed": app.date_listed,
        "date_applied": app.date_applied,
        "follow_up": app.follow_up,
        "result": app.result,
        "contacts": app.contacts,
        "notes": app.notes
    }
    return render(response, "main/home.html", context)


def add(response):
    if response.method == "POST":
        form = AddApplication(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
           
    return render(response, "main/add.html", {})
