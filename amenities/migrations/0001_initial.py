# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'amenity',
            },
        ),
        migrations.CreateModel(
            name='amenity_inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('idAmenity', models.ForeignKey(to='amenities.amenity')),
            ],
            options={
                'db_table': 'amenity_inmueble',
            },
        ),
        migrations.CreateModel(
            name='division_amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=75)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'division_amenity',
            },
        ),
    ]
