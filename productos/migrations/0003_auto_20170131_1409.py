# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20170131_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
        migrations.RenameModel(
            old_name='Productos_Categorias',
            new_name='Productos_Categoria',
        ),
        migrations.RenameModel(
            old_name='Productos_Etiquetas',
            new_name='Productos_Etiqueta',
        ),
    ]
