from django.db import models

# Create your models here.
class ApplicationList(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

class Application(models.Model):
    applicationlist = models.ForeignKey(ApplicationList, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date_listed = models.DateField()
    date_applied = models.DateField()
    follow_up = models.BooleanField()
    result = models.CharField(max_length=20)
    contacts = models.CharField(max_length=200)

    def __str__(self):
        return self.company, self.job_title, self.date_listed, self.date_applied,self.follow_up, self.result, self.contacts

    
    

