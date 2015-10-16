from django.db import models
from usuarios.models import *

class tipoCliente(models.Model):
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return description

	class Meta:
		db_table = 'tipo_cliente'

class estadoCliente(models.Model):
	description = models.CharField(max_length=25)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return description

	class Meta:
		db_table = 'estado_cliente'

class Cliente(models.Model):
	idTipoCliente = models.ForeignKey(tipoCliente)
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=15)
	cellphone_number = models.CharField(max_length=15, null=True)
	address = models.CharField(max_length=150, null=True)
	email = models.EmailField(max_length=150)
	idEstadoCliente = models.ForeignKey(estadoCliente)
	last_action = models.CharField(max_length=200, null=True)
	idVendedorAsignado = models.ForeignKey('usuarios.usuario')
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'cliente'

class notasCliente(models.Model):
	idCliente = models.ForeignKey(Cliente)
	idUsuario = models.ForeignKey('usuarios.usuario')
	note = models.TextField(max_length=500)
	date_note = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'notas_cliente'