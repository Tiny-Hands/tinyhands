# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-07-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0255_auto_20230707_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationinformation',
            name='pvs_visited',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='locationinformation',
            name='suspects_associative',
            field=models.TextField(null=True),
        ),
    ]