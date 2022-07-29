from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email_department = models.EmailField(max_length=200)