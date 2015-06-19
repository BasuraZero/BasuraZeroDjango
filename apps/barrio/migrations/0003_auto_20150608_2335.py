# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barrio', '0002_auto_20150608_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calle',
            name='dia',
            field=models.ManyToManyField(to='barrio.Dia'),
        ),
    ]
