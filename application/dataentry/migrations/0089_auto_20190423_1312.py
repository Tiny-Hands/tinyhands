# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-23 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0088_auto_20190418_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='cifattachmentindia',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cifattachmentnepal',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='irfattachmentbangladesh',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='irfattachmentindia',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='irfattachmentsouthafrica',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vdfattachmentindia',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vdfattachmentnepal',
            name='private_card',
            field=models.BooleanField(default=True),
        ),
    ]
