# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default='true'),
        ),
    ]
