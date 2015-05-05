# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_reviewusuario'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tipousuario',
            table='tipo_usuario',
        ),
    ]
