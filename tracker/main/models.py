from django.db import models

# Create your models here.
class ApplicationList(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

class Applications(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_listed = models.DateField()
    date_applied = models.DateField()
    follow_up = models.BooleanField(default=False)
    result = models.CharField(max_length=20)
    contacts = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.text

    
    

