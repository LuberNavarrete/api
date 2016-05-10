# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160509_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fecha_fin',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fecha_inicio',
        ),
    ]
