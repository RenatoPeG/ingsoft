from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    vida = models.IntegerField()
    icono = models.CharField(max_length=500)

    def __str__(self):
        cad = self.nombre + ' - ' \
              + str(self.vida) + ' - ' \
              + str(self.icono)
        return cad
