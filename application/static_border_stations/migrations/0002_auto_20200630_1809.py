# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-06-30 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_border_stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='first_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='location',
            name='last_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='location_type',
            field=models.CharField(default='monitoring', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='first_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_date',
            field=models.DateField(null=True),
        ),
    ]
