# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0002_auto_20161229_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='default_coda',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='default_pos',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='default_segmentation',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
