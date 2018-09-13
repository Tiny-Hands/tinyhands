# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-13 08:55
from __future__ import unicode_literals

from django.db import migrations, models

from dataentry.models.form_migration import FormMigration

def migrate_forms(apps, schema_editor):
    # Invoke form migration with specific file containing lastest form data
    FormMigration.migrate(apps, schema_editor, 'form_data_20180913.json')

class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0065_auto_20180907_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='irfindia',
            name='reason_for_intercept',
        ),
        migrations.RemoveField(
            model_name='irfmalawi',
            name='reason_for_intercept',
        ),
        migrations.RemoveField(
            model_name='irfnepal',
            name='reason_for_intercept',
        ),
        migrations.AddField(
            model_name='irfindia',
            name='case_notes',
            field=models.TextField(blank=True, verbose_name='Case Notes'),
        ),
        migrations.AddField(
            model_name='irfmalawi',
            name='case_notes',
            field=models.TextField(blank=True, verbose_name='Case Notes'),
        ),
        migrations.AddField(
            model_name='irfnepal',
            name='case_notes',
            field=models.TextField(blank=True, verbose_name='Case Notes'),
        ),
        migrations.AlterField(
            model_name='irfbangladesh',
            name='known_place_bangladesh',
            field=models.CharField(default='False', max_length=127),
        ),
        migrations.RunPython(migrate_forms),
    ]
