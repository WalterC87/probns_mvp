# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20150901_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('cellphone_number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('last_action', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='estadoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=25)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'estado_cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='notasCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(max_length=500)),
                ('date_note', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('idCliente', models.ForeignKey(to='clientes.Cliente')),
                ('idUsuario', models.ForeignKey(to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'notas_cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tipoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tipo_cliente',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='idEstadoCliente',
            field=models.ForeignKey(to='clientes.estadoCliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idTipoCliente',
            field=models.ForeignKey(to='clientes.tipoCliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idVendedorAsignado',
            field=models.ForeignKey(to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
