from django.db import models
from usuarios.models import *
from inmuebles.models import *

class red_social(models.Model):
	description = models.CharField(max_length=50)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'red_social'

class share_inmueble(models.Model):
	idInmueble = models.ForeignKey('inmuebles.inmueble')
	idUsuario = models.ForeignKey('usuarios.usuario')
	idRedSocial = models.ForeignKey(red_social)
	share_date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'share_inmueble'

class tracking_inmueble(models.Model):
	idInmueble = models.ForeignKey('inmuebles.inmueble')
	idUsuario = models.ForeignKey('usuarios.usuario')
	tracking_date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'tracking_inmueble'
