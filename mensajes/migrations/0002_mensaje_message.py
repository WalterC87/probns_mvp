# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
