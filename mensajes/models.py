from django.db import models
from inmuebles.models import *
from usuarios.models import *

class tipo_mensaje(models.Model):
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tipo_mensaje'

class accion_mensaje(models.Model):
	description = models.CharField(max_length=50)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'accion_mensaje'

class mensaje(models.Model):
	idTipoMensaje = models.ForeignKey(tipo_mensaje)
	idAccionMensaje = models.ForeignKey(accion_mensaje)
	idRemitente = models.ForeignKey('usuarios.usuario', related_name='remitente')
	idDestinatario = models.ForeignKey('usuarios.usuario', related_name='destinatario')
	message = models.TextField()
	message_date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'mensaje'