# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-08 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('accounts', '0012_auto_20180126_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringToken',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('authtoken.token',),
        ),
    ]
