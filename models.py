from django.db import models

class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField( max_length=100)

# Create your models here.
