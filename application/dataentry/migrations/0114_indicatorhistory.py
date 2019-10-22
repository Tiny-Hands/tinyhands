# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-10-08 13:19
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0113_auto_20190909_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('month', models.PositiveIntegerField(verbose_name='Month')),
                ('indicators', django.contrib.postgres.fields.jsonb.JSONField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Country')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='verification_goals',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='verification_start_month',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='verification_start_year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
