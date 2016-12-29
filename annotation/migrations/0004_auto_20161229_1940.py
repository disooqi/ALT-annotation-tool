# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0003_auto_20161229_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenoccurrence',
            name='coda',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tokenoccurrence',
            name='pos',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tokenoccurrence',
            name='segmentation',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
