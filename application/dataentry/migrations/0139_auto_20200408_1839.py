# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-04-08 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0138_milawi_sierra_irf'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyreport',
            name='govern_coord_accounting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='govern_coord_awareness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='govern_coord_shelter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='records_verified_phone_percent',
            field=models.CharField(max_length=126, null=True),
        ),
    ]
