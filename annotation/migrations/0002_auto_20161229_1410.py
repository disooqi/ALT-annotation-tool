# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='id',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_id',
            field=models.IntegerField(default=-1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
