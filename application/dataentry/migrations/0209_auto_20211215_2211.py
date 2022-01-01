# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-15 22:11
from __future__ import unicode_literals

import dataentry.models.border_station
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0208_auto_20211207_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('sort_order', models.PositiveIntegerField(default=999)),
            ],
        ),
        migrations.AddField(
            model_name='borderstation',
            name='features',
            field=models.CharField(default='hasStaff;hasSubcommittee;hasProjectStats;hasLocations;hasLocationStaffing;hasForms', max_length=512),
        ),
        migrations.AddField(
            model_name='borderstation',
            name='project_category',
            field=models.ForeignKey(default=dataentry.models.border_station.get_border_station_default_category, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.ProjectCategory'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='min_level',
            field=models.CharField(default='PROJECT', max_length=100),
        ),
    ]
