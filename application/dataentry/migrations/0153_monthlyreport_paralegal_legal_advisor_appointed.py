# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-09-17 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0152_vdf_v2'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyreport',
            name='paralegal_legal_advisor_appointed',
            field=models.CharField(max_length=126, null=True),
        ),
    ]
