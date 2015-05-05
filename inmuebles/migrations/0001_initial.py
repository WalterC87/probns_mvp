# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0001_initial'),
        ('usuarios', '0007_auto_20150426_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'estado_inmueble',
            },
        ),
        migrations.CreateModel(
            name='imagenes_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images_property')),
                ('description', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'db_table': 'imagenes_inmueble',
            },
        ),
        migrations.CreateModel(
            name='inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_property', models.DecimalField(max_digits=18, decimal_places=2)),
                ('short_address', models.CharField(max_length=75)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=50, blank=True)),
                ('longitude', models.CharField(max_length=50, blank=True)),
                ('construction_area', models.DecimalField(max_digits=10, decimal_places=2)),
                ('property_extention', models.DecimalField(max_digits=10, decimal_places=2)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('observations', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('idDepartamento', models.ForeignKey(to='paises.departamento')),
                ('idEstadoInmueble', models.ForeignKey(to='inmuebles.estado_inmueble')),
                ('idMoneda', models.ForeignKey(to='paises.moneda')),
                ('idMunicipio', models.ForeignKey(to='paises.municipio')),
            ],
            options={
                'db_table': 'inmueble',
            },
        ),
        migrations.CreateModel(
            name='inmuebles_favoritos_usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1200, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'inmuebles_favoritos_usuario',
            },
        ),
        migrations.CreateModel(
            name='inmuebles_usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('sold_date', models.DateTimeField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'inmuebles_usuario',
            },
        ),
        migrations.CreateModel(
            name='operacion_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'operacion_inmueble',
            },
        ),
        migrations.CreateModel(
            name='review_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1200)),
                ('status', models.BooleanField(default=True)),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
                ('idPadre', models.ForeignKey(to='inmuebles.review_inmueble')),
            ],
            options={
                'db_table': 'review_inmueble',
            },
        ),
        migrations.CreateModel(
            name='tipo_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tipo_inmueble',
            },
        ),
        migrations.AddField(
            model_name='inmueble',
            name='idOperacionInmueble',
            field=models.ForeignKey(to='inmuebles.operacion_inmueble'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='idPais',
            field=models.ForeignKey(to='paises.pais'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='idTipoInmueble',
            field=models.ForeignKey(to='inmuebles.tipo_inmueble'),
        ),
        migrations.AddField(
            model_name='imagenes_inmueble',
            name='idInmueble',
            field=models.ForeignKey(to='inmuebles.inmueble'),
        ),
    ]
