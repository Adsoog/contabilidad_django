# models.py
from django.db import models


class TuModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    # Agrega más campos según sea necesario
