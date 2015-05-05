# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20150426_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewusuario',
            name='idUsuarioReview',
            field=models.ForeignKey(related_name='idUserReview', default=1, to='usuarios.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewusuario',
            name='idUsuario',
            field=models.ForeignKey(related_name='idUsuario', to='usuarios.Usuario'),
        ),
    ]
