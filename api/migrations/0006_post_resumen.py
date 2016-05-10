# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160405_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resumen',
            field=models.CharField(max_length=100, null=True, editable=False, blank=True),
        ),
    ]
