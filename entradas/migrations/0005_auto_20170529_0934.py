# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0004_auto_20170206_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='comentario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entradas.Comentario_Entrada'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/entradas'),
        ),
    ]
