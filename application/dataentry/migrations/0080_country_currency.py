# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-08 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0079_cifattachmentnepal'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.CharField(blank=True, max_length=127),
        ),
    ]