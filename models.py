from django.db import models

# Create your models here.

class Oxygen_Leads(models.Model):
    Address = models.CharField(max_length=200)
    Business_Name = models.CharField(max_length = 30)
    Person_Name = models.CharField(max_length = 30)
    Contact = models.CharField(max_length = 12)
    Verified_Status = models.CharField(max_length = 30)
    TimeStamp = models.DateTimeField(auto_now_add=True)
