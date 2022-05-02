from django.db import models

# Create your models here.

class sign_up_model(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100, primary_key=True)
    password=models.CharField(max_length=100)