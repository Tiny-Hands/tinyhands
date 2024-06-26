# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-09-15 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0196_auto_20210909_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_bus_driver_payment_at_destination',
            field=models.BooleanField(default=False, verbose_name='Bus driver expecting payment for travel at destination'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_first_time_traveling_to_city',
            field=models.BooleanField(default=False, verbose_name='Travelling to city from rural area for first time'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_no_id',
            field=models.BooleanField(default=False, verbose_name='Does not have any form of ID'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_no_mobile_phone',
            field=models.BooleanField(default=False, verbose_name='Does not own mobile phone'),
        ),
    ]
