from django.db import models

class Cliente(models.Model):
	Sexo = (
		('Hombre','Hombre'),
		('Mujer','Mujer'),
	)

	'''
	 <<<< INFO GENERAL DEL CLIENTE >>>>
	'''
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10,choices=Sexo)
	telefono_1 = models.CharField(max_length=25)
	telefono_2 = models.CharField(max_length=25, blank=True)
	email = models.EmailField()
	fecha_registro = models.DateTimeField(auto_now=True)
	'''
	 <<<< DIRECCION DEL CLIENTE >>>>
	'''
	calle = models.CharField(max_length=50,blank=True)
	colonia = models.CharField(max_length=50,blank=True)
	codigo_postal = models.CharField(max_length=5,blank=True)
	municipio = models.CharField(max_length=50,default='Acapulco de Juarez')
	estado = models.CharField(max_length=50,default='Guerrero')
	descripcion = models.TextField(blank=True)
	
	class Meta:
		ordering = ["id"]

	def __str__(self):
		return "{0} {1} {2}".format(self.nombre,self.apellido_paterno,self.apellido_materno)

class Asesore(models.Model):
	Sexo = (
		('Hombre','Hombre'),
		('Mujer','Mujer'),
	)

	'''
	 <<<< INFO GENERAL DEL ASESOR >>>>
	'''
	nombre = models.CharField(max_length=100)
	sexo = models.CharField(max_length=10 ,choices=Sexo)
	email = models.EmailField()

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return "{0}".format(self.nombre)

	def completo(self):
		return "{0}".format(self.nombre)

	completo.short_description = 'Nombre del Asesor'


class Telefono(models.Model):
	asesor = models.ForeignKey(Asesore)
	numero = models.CharField(max_length=15)

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return "{}".format(self.asesor)
	

class BolsaInmobiliaria(models.Model):
	tipo_cambio = (
		('MN','MN'),
		('USD','USD'),
	)

	asesor = models.ForeignKey(Asesore)
	descripcion = models.TextField()
	ubicacion = models.CharField(max_length=100)
	precio = models.IntegerField()
	fecha_registro = models.DateField(auto_now=True)
	moneda = models.CharField(max_length=10,choices=tipo_cambio)

	class Meta:
		ordering = ["id"]

	def __str__(self):
		return "{0} - {1}".format(self.asesor,(self.descripcion).split())