# from rest_framework import routers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Application
from .forms import AddApplication, EditApplication

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
            # com = form.cleaned_data['company']
            # jt = form.cleaned_data['job_title']
            # dl = form.cleaned_data['date_listed']
            # da = form.cleaned_data['date_applied']
            # r =form.cleaned_data['result']
            # con =form.cleaned_data['contacts']
            # n =form.cleaned_data['notes']
            # l = form.cleaned_data['link']
            # a = Application(company=com, job_title=jt, date_listed=dl, date_applied=da, result=r, contacts=con, notes=n, link=l)
            form.save()

        return redirect('/')

    else:
        form = AddApplication()
   
    return render(response, "main/add.html", {'form': form})



def edit(response, id):
    application = Application.objects.get(id=id)
    if response.method == "PUT":
        form = EditApplication(response.PUT, instance=application)

        if form.is_valid():
            r =form.cleaned_data['result'] 
            n =form.cleaned_data['notes']          
            a = Application(result=r, notes=n)
            a.objects.update()

        return redirect('/')

    else:
        form = EditApplication()

    return render(response, 'main/edit.html', {'a': application, 'form': form})

