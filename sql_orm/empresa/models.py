from django.db import models

class Departamento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.IntegerField()

    def __str__(self):
    	return "{0} - {1}".format(self.codigo,self.nombre)
 
class Empleado(models.Model):
	clave = models.CharField(primary_key=True,max_length=8)
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=255)
	departamento = models.ForeignKey(Departamento)

	def __str__(self):
		return "{0} {1}".format(self.nombre,self.apellidos)