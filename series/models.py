from django.db import models
from django.utils import timezone

# Create your models here.
class Serie(models.Model):
    serie = models.CharField(max_length=200)
    temporadas = models.CharField(max_length=200)
    finalizado = models.BooleanField()
    visto = models.DateField(
            blank=True, null=True)
    def __str__(self):
        return self.serie
