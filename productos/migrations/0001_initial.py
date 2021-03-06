# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('stock', models.CharField(max_length=20)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('imagen', models.ImageField(upload_to=b'')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Etiquetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Productos_Categorias'),
        ),
        migrations.AddField(
            model_name='productos',
            name='etiqueta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Productos_Etiquetas'),
        ),
        migrations.AddField(
            model_name='productos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuarios'),
        ),
    ]
