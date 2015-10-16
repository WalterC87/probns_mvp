# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('inmuebles', '0002_inmueble_year_construction'),
    ]

    operations = [
        migrations.CreateModel(
            name='inmuebles_cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('sold_date', models.DateTimeField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('idCliente', models.ForeignKey(to='clientes.Cliente')),
                ('idInmueble', models.ForeignKey(to='inmuebles.inmueble')),
            ],
            options={
                'db_table': 'inmuebles_cliente',
            },
            bases=(models.Model,),
        ),
    ]
