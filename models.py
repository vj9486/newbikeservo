from django.db import models

# Create your models here.
class fillform(models.Model):
    time=models.CharField( max_length=50)
    name=models.CharField(max_length=50)
    
