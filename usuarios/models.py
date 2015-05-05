from django.db import models

# Create your models here.

class tipoUsuario(models.Model):
	description = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.description

	class Meta:
		db_table = 'tipo_usuario'


class Usuario(models.Model):
	idTipoUsuario = models.ForeignKey(tipoUsuario)
	name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150, blank=True)
	email = models.EmailField(max_length=150)
	website = models.CharField(max_length=150, blank=True)	
	password = models.CharField(max_length=450)
	avatar = models.ImageField(upload_to='avatars')
	address = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=15)
	description = models.CharField(max_length=1000)
	creation_date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'usuario'

class reviewUsuario(models.Model):
	idUsuario = models.ForeignKey(Usuario, related_name='idUsuario')
	idUsuarioReview = models.ForeignKey(Usuario, related_name='idUserReview')
	review = models.CharField(max_length=1250)
	ranking = models.IntegerField
	status = models.BooleanField(default=True)

	class Meta:
		db_table = 'review_usuario'