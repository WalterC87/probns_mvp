# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20150426_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='accion_mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'accion_mensaje',
            },
        ),
        migrations.CreateModel(
            name='mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('idAccionMensaje', models.ForeignKey(to='mensajes.accion_mensaje')),
                ('idDestinatario', models.ForeignKey(related_name='destinatario', to='usuarios.Usuario')),
                ('idRemitente', models.ForeignKey(related_name='remitente', to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'mensaje',
            },
        ),
        migrations.CreateModel(
            name='tipo_mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tipo_mensaje',
            },
        ),
        migrations.AddField(
            model_name='mensaje',
            name='idTipoMensaje',
            field=models.ForeignKey(to='mensajes.tipo_mensaje'),
        ),
    ]
