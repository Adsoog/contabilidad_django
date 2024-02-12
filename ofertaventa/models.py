from django.db import models

# Create your models here.

class Inventario(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=225)
    age = models.CharField(max_length=225)
    monthly_salary = models.CharField(max_length=1000)