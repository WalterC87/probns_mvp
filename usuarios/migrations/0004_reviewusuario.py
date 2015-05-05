# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20150426_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.CharField(max_length=1250)),
                ('status', models.BooleanField(default=True)),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
        ),
    ]
