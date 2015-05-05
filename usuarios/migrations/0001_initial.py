# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150, blank=True)),
                ('email', models.EmailField(max_length=150)),
                ('website', models.CharField(max_length=150, blank=True)),
                ('password', models.CharField(max_length=500)),
                ('avatar', models.ImageField(upload_to=b'avatars')),
                ('address', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('idTipoUsuario', models.ForeignKey(to='usuarios.tipoUsuario')),
            ],
        ),
    ]
