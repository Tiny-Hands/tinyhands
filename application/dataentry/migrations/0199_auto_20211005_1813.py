# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-05 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0198_auto_20210929_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='cifcommon',
            name='border_cross_na',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cifcommon',
            name='legal_action_taken_staff_thi_does_not_believe',
            field=models.BooleanField(default=False),
        ),
    ]
