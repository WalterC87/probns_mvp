from django.db import models

# Create your models here.

class pais(models.Model):
	description = models.CharField(max_length=100)
	flag = models.ImageField(upload_to='flags')
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'pais'

class departamento(models.Model):
	idPais = models.ForeignKey(pais)
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'departamento'

class municipio (models.Model):
	idDepartamento = models.ForeignKey(departamento)
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'municipio'

class moneda(models.Model):
	idPais = models.ForeignKey(pais)
	description = models.CharField(max_length=50)
	simbolo = models.CharField(max_length=5)
	status = models.BooleanField(default=True)
