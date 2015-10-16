from django.db import models
from paises.models import *
from usuarios.models import *
from clientes.models import *

class tipo_inmueble(models.Model):
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tipo_inmueble'

class operacion_inmueble(models.Model):
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'operacion_inmueble'

class estado_inmueble(models.Model):
	description = models.CharField(max_length=50)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'estado_inmueble'

class inmueble(models.Model):
	idTipoInmueble = models.ForeignKey(tipo_inmueble)
	idEstadoInmueble = models.ForeignKey(estado_inmueble)
	idOperacionInmueble = models.ForeignKey(operacion_inmueble)
	idMoneda = models.ForeignKey('paises.moneda')
	idPais = models.ForeignKey('paises.pais')
	idDepartamento = models.ForeignKey('paises.departamento')
	idMunicipio = models.ForeignKey('paises.municipio')
	price_property = models.DecimalField(max_digits=18,decimal_places=2)
	short_address = models.CharField(max_length=75)
	address = models.CharField(max_length=200)
	latitude = models.CharField(max_length=50, blank=True)
	longitude = models.CharField(max_length=50, blank=True)
	construction_area = models.DecimalField(max_digits=10,decimal_places=2)
	property_extention = models.DecimalField(max_digits=10,decimal_places=2)
	year_construction = models.PositiveIntegerField()
	creation_date = models.DateTimeField(auto_now_add=True)
	release_date = models.DateTimeField(auto_now_add=True)
	observations = models.TextField(blank=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'inmueble'

class imagenes_inmueble(models.Model):
	idInmueble = models.ForeignKey(inmueble)
	image = models.ImageField(upload_to='images_property')
	description = models.CharField(max_length=150, blank=True)
	
	class Meta:
		db_table = 'imagenes_inmueble'

class inmuebles_usuario(models.Model):
	idUsuario = models.ForeignKey('usuarios.usuario')
	idInmueble = models.ForeignKey(inmueble)
	assigned_date = models.DateTimeField(auto_now_add=True)
	sold_date = models.DateTimeField(auto_now_add=False, blank=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'inmuebles_usuario'

class inmuebles_cliente(models.Model):
	idCliente = models.ForeignKey('clientes.cliente')
	idInmueble = models.ForeignKey(inmueble)
	assigned_date = models.DateTimeField(auto_now_add=True)
	sold_date = models.DateTimeField(auto_now_add=False, blank=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'inmuebles_cliente'

class review_inmueble(models.Model):
	idPadre = models.ForeignKey('self')
	idInmueble = models.ForeignKey(inmueble)
	comment = models.CharField(max_length=1200)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'review_inmueble'

class inmuebles_favoritos_usuario(models.Model):
	idUsuario = models.ForeignKey('usuarios.usuario')
	idInmueble = models.ForeignKey(inmueble)
	comment = models.CharField(max_length=1200,blank=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'inmuebles_favoritos_usuario'