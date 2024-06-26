# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-30 16:16
from __future__ import unicode_literals
import os

from django.db import migrations, models
from django.core.management import call_command

app_name = 'dataentry'

form_model_names = [
    'FormType',
    'Storage',
    "Form",
    'CategoryType',
    'Category',
    'CardStorage',
    'AnswerType',
    'Question',
    'QuestionLayout',
    'QuestionStorage',
    'Answer',
    'FormValidationLevel',
    'FormValidationType',
    'FormValidation',
    'FormValidationQuestion',
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0056_merge_20180724_1837'),
    ]
    
    def load_fixture(apps, schema_editor):
        fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fixtures'))
        fixture_filename = 'form_data_20180801.json'
        fixture_file = os.path.join(fixture_dir, fixture_filename)
        call_command('loaddata', fixture_file) 
    
    def unload_prior(apps, schema_editor):
        for model_name in reversed(form_model_names):
            my_model = apps.get_model(app_name, model_name)
            my_model.objects.all().delete()

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='country',
        ),
        migrations.AddField(
            model_name='form',
            name='form_name',
            field=models.CharField(default='temp', max_length=126),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='stations',
            field=models.ManyToManyField(to='dataentry.BorderStation'),
        ),
        migrations.RunSQL("INSERT INTO dataentry_permission (permission_group, action, min_level, account_permission_name) values ('STATIONS', 'SET_FORMS','GLOBAL',null);"),
        #migrations.RunPython(unload_prior),
        #migrations.RunPython(load_fixture),
    ]
