# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-27 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0012_borderstationbudgetcalculation_date_finalized'),
    ]

    operations = [
        migrations.AddField(
            model_name='borderstationbudgetcalculation',
            name='past_sent_approved',
            field=models.CharField(blank=True, max_length=127),
        ),
    ]
