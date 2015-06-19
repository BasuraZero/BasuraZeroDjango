# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barrio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='calle',
            name='dia',
            field=models.ManyToManyField(to='barrio.Dia', verbose_name=b'list of dia'),
        ),
    ]
