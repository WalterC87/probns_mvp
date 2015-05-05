# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0001_initial'),
        ('usuarios', '0007_auto_20150426_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='red_social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'red_social',
            },
        ),
        migrations.CreateModel(
            name='share_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
                ('idRedSocial', models.ForeignKey(to='trackings.red_social')),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'share_inmueble',
            },
        ),
        migrations.CreateModel(
            name='tracking_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'tracking_inmueble',
            },
        ),
    ]
