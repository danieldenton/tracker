from django.db import models
from datetime import date

# Create your models here.

class Application(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_listed = models.DateField(default=date.today)
    date_applied = models.DateField(default=date.today)
    follow_up = models.BooleanField()
    result = models.CharField(max_length=20)
    contacts = models.CharField(max_length=200)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.company, self.job_title, self.date_listed, self.date_applied,self.follow_up, self.result, self.contacts, self.notes

    
    

