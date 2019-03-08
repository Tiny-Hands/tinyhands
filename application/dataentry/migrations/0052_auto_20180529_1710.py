# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-29 17:10
from __future__ import unicode_literals
import os

from django.db import migrations
from django.core.management import call_command
from django.core.management.color import no_style
from django.db import connection

from dataentry.models import Country

app_name = 'dataentry'

country_names = [
    'Nepal',
    'South Africa',
    'Thailand',
    'India'
    ]
 
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
        ('dataentry', '0051_formvalidation_trigger_value'),
    ]
    
    def ensure_countries(apps, schema_editor):
        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Country,])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

    def load_fixture(apps, schema_editor):
        fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fixtures'))
        fixture_filename = 'form_data_20180531.json'
        fixture_file = os.path.join(fixture_dir, fixture_filename)
        call_command('loaddata', fixture_file) 
    
    def unload_prior(apps, schema_editor):
        for model_name in reversed(form_model_names):
            my_model = apps.get_model(app_name, model_name)
            my_model.objects.all().delete()

    operations = [
        migrations.RunSQL("INSERT INTO dataentry_country (id, name, latitude, longitude, zoom_level) values (1, 'Nepal',0,0,0) on conflict do nothing;"),
        migrations.RunSQL("INSERT INTO dataentry_country (id, name, latitude, longitude, zoom_level) values (2, 'South Africa',0,0,0) on conflict do nothing;"),
        migrations.RunSQL("INSERT INTO dataentry_country (id, name, latitude, longitude, zoom_level) values (3, 'Thailand',0,0,0) on conflict do nothing;"),
        migrations.RunSQL("INSERT INTO dataentry_country (id, name, latitude, longitude, zoom_level) values (4, 'India',0,0,0) on conflict do nothing;"),
        
        migrations.RunPython(ensure_countries)
    ]
