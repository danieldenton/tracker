# from rest_framework import routers
from django.shortcuts import render, redirect
from .models import  Application
from .forms import ApplicationForm

def home(request):
    application = Application.objects.all()
    context = {
        'application': application
         } 

    return render(request, "main/home.html", context)


def add(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
        
   
    return render(request, "main/add.html", {'form': form})



def edit(request, id):
    application = Application.objects.get(id=id)
    form = ApplicationForm(instance=application)
    context = {'form': form}
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid(): 
            form.save(commit=False)

        return redirect('/')

    elif request.method == "DELETE":
        form = ApplicationForm(request.DELETE, instance=application)
        if form.is_valid(): 
            form.object.update()

        return redirect('/')


    return render(request, 'main/edit.html', context)

