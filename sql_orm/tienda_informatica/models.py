from django.db import models

class Fabricante(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
    	return "{0}".format(self.nombre)


class Articulo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    fabricante = models.ForeignKey(Fabricante)

    def __str__(self):
    	return "{0} - {1}".format(self.fabricante,self.nombre)

    class Meta:
    	ordering = ['codigo']



 