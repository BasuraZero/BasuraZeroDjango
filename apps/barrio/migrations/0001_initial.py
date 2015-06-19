# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreBarrio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreCalle', models.CharField(max_length=50)),
                ('num_maximo', models.IntegerField(null=True, blank=True)),
                ('num_minimo', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='calle',
            name='hora',
            field=models.ForeignKey(to='barrio.Hora'),
        ),
        migrations.AddField(
            model_name='calle',
            name='nombreBarrio',
            field=models.ForeignKey(to='barrio.Barrio'),
        ),
    ]
