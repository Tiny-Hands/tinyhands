# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-14 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0066_auto_20180913_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checksum', models.IntegerField()),
                ('blocks', models.IntegerField()),
            ],
        ),
    ]
