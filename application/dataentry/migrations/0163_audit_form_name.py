# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-11-03 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0162_auto_20201029_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='form_name',
            field=models.CharField(default='temp', max_length=126),
            preserve_default=False,
        ),
        
        migrations.RunSQL("update dataentry_audit set form_name = (select form_name from dataentry_form where id=dataentry_audit.form_id)"),
    ]
