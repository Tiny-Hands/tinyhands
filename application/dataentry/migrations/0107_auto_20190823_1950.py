# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-23 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0106_auto_20190801_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercepteebangladesh',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteebenin',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteeghana',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteeindia',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteekenya',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteemalawi',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteenepal',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteesierraleone',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteesouthafrica',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteetanzania',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='intercepteeuganda',
            name='anonymized_photo',
            field=models.CharField(max_length=126, null=True),
        ),
    ]
