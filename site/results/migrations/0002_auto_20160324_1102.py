# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.Runner'),
        ),
    ]
