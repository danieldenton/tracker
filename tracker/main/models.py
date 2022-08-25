from django.db import models
from datetime import date

# Create your models here.

class Application(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_listed = models.DateField(default=date.today required=False))
    date_applied = models.DateField(default=date.today)
    result = models.CharField(max_length=20 required=False)
    contacts = models.CharField(max_length=200)
    notes = models.CharField(max_length=300 required=False))
    link = models.CharField(max_length=200)

    def __repr__(self):
        return 'Object: {}' .format(self.company, self.job_title, self.date_listed, self.date_applied, self.follow_up, self.result, self.contacts, self.notes)

    
    

