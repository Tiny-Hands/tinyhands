# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-07-12 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0190_auditsample_no_paper_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='form_version',
            field=models.CharField(blank=True, max_length=126),
        ),
        migrations.AddField(
            model_name='cifcommon',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='gospelverification',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='legalcase',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='monthlyreport',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='form_version',
            field=models.CharField(max_length=126, null=True),
        ),
    ]