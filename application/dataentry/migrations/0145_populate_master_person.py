# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-05-14 13:46
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from dataentry.models.master_person import MasterPerson
from dataentry.models.person import Person

def create_master_persons(apps, schema_editor):
    # Create and link master person for those persons that have alias groups
    persons = Person.objects.filter(alias_group__isnull=False).order_by('alias_group__id', 'id')
    last_alias_group = None
    for person in persons:
        if last_alias_group is None or last_alias_group != person.alias_group:
            master_person = MasterPerson()
        
        last_alias_group = person.alias_group
        
        master_person.update(person)
        master_person.save()
        person.master_person = master_person
        person.save()
    
    # Create new master person for each person not in alias group        
    persons = Person.objects.filter(master_person__id=0)
    for person in persons:
        master_person = MasterPerson()
        master_person.update(person)
        master_person.save()
        person.master_person = master_person
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0144_add_master_person_model'),
    ]

    operations = [
        migrations.RunPython(create_master_persons),
    ]
