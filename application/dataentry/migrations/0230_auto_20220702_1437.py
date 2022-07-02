# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-02 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0229_storage_form_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='form_model_name',
            field=models.CharField(max_length=126),
        ),
        migrations.AlterField(
            model_name='storage',
            name='form_tag',
            field=models.CharField(max_length=126, unique=True),
        ),
    ]
