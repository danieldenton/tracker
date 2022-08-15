from django.contrib import admin
from .models import ApplicationList, Application

# Register your models here.
admin.site.register(ApplicationList)
admin.site.register(Application)