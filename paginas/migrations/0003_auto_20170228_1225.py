# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_auto_20170131_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='slugs',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
