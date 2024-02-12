from django.db import models

# Create your models here.
class Inventory(models.Model):

    id_sap= models.CharField(max_length=150)
    item = models.CharField(max_length=200)
    precio_unitario = models.CharField(max_length=10000)
