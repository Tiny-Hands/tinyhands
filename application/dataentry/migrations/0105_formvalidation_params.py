# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-16 13:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0104_country_mdf_sender_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='formvalidation',
            name='params',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
