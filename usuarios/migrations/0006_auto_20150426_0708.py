# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20150426_0707'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='reviewusuario',
            table='review_usuario',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]
