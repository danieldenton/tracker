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
            com = form.cleaned_data['company']
            jt = form.cleaned_data['job_title']
            dl = form.cleaned_data['date_listed']
            da = form.cleaned_data['date_applied']
            fu = form.cleaned_data['follow_up']
            r =form.cleaned_data['result']
            con =form.cleaned_data['contacts']
            n =form.cleaned_data['notes']
            l = form.cleaned_data['link']
            a = Application(company=com, job_title=jt, date_listed=dl, date_applied=da,follow_up=fu, result=r, contacts=con, notes=n, link=l)
            a.save()

        return HttpResponseRedirect("/l")

    else:
        form = AddApplication()

    
        
    return render(response, "main/add.html", {'form': form})
