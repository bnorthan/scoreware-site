# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_auto_20160413_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
