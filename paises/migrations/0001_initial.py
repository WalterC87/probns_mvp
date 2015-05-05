# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'departamento',
            },
        ),
        migrations.CreateModel(
            name='moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('simbolo', models.CharField(max_length=5)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('idDepartamento', models.ForeignKey(to='paises.departamento')),
            ],
            options={
                'db_table': 'municipio',
            },
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('flag', models.ImageField(upload_to=b'flags')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'pais',
            },
        ),
        migrations.AddField(
            model_name='moneda',
            name='idPais',
            field=models.ForeignKey(to='paises.pais'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='idPais',
            field=models.ForeignKey(to='paises.pais'),
        ),
    ]
