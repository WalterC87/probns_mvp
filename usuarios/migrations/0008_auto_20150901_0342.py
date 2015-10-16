# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20150426_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewusuario',
            name='ranking',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewusuario',
            name='idUsuario',
            field=models.ForeignKey(related_name='Usuario', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewusuario',
            name='idUsuarioReview',
            field=models.ForeignKey(related_name='UserReview', to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
