# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_post_resumen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='imagen',
            new_name='src',
        ),
    ]
