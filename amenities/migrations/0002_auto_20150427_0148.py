# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amenities', '0001_initial'),
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity_inmueble',
            name='idInmueble',
            field=models.ForeignKey(to='inmuebles.inmueble'),
        ),
        migrations.AddField(
            model_name='amenity',
            name='idDivisionAmenity',
            field=models.ForeignKey(to='amenities.division_amenity'),
        ),
    ]
