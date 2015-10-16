# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amenities', '0002_auto_20150427_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity_inmueble',
            name='Cantidad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
