# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-07-07 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0189_stationstatistics_subcommittee_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditsample',
            name='no_paper_form',
            field=models.BooleanField(default=False, verbose_name='No Paper form'),
        ),
    ]
