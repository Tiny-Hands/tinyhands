# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-10-27 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20230302_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
