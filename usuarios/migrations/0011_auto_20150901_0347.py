# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20150901_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewusuario',
            name='idUsuario',
            field=models.ForeignKey(related_name='idUsuario', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewusuario',
            name='idUsuarioReview',
            field=models.ForeignKey(related_name='idUserReview', to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
