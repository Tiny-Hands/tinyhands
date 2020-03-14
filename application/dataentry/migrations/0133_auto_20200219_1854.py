# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-19 18:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0132_auto_20200212_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationboxcommon',
            name='address',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='locationboxcommon',
            name='address_notes',
            field=models.TextField(blank=True, verbose_name='Address Notes'),
        ),
        migrations.AddField(
            model_name='locationboxcommon',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='locationboxcommon',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='address_notes',
            field=models.TextField(blank=True, verbose_name='Address Notes'),
        ),
        migrations.AddField(
            model_name='person',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
