# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token_text', models.CharField(max_length=15)),
                ('default_coda', models.CharField(max_length=15)),
                ('default_segmentation', models.CharField(max_length=15)),
                ('default_pos', models.CharField(max_length=15)),
                ('ambiguous', models.BooleanField(default=False)),
                ('freq', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TokenOccurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('coda', models.CharField(max_length=15)),
                ('segmentation', models.CharField(max_length=15)),
                ('pos', models.CharField(max_length=15)),
                ('token', models.ForeignKey(to='annotation.Token')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_text', models.CharField(max_length=140)),
                ('members', models.ManyToManyField(to='annotation.Token', through='annotation.TokenOccurrence')),
            ],
        ),
        migrations.AddField(
            model_name='tokenoccurrence',
            name='tweet',
            field=models.ForeignKey(to='annotation.Tweet'),
        ),
    ]
