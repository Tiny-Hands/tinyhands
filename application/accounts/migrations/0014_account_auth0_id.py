# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-14 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_expiringtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='auth0_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
