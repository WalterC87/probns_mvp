from django.db import models
from usuarios.models import *
from inmuebles.models import *

class division_amenity(models.Model):
	description = models.CharField(max_length=75)
	status = models.BooleanField(default=True)

	class Meta:
		db_table='division_amenity'

class amenity(models.Model):
	idDivisionAmenity = models.ForeignKey(division_amenity)
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'amenity'

class amenity_inmueble(models.Model):
	idInmueble = models.ForeignKey('inmuebles.inmueble')
	idAmenity = models.ForeignKey(amenity)
	Cantidad = models.PositiveIntegerField(default=0)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'amenity_inmueble'