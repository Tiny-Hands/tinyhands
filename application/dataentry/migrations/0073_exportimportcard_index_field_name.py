# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-08 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0072_merge_20181106_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportimportcard',
            name='index_field_name',
            field=models.CharField(max_length=126, null=True),
        ),
    ]
