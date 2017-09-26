from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    vida = models.IntegerField()

    def __str__(self):
        return self.nombre + ' - ' + str(self.vida)