from django.db import models

class Familiar(models.Model):
    numero = models.IntegerField()
    cadena = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.cadena

    class Meta:
        app_label = 'familiares'

