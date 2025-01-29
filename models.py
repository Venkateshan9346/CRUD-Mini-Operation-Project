from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField(max_length=50)