# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 21:24
from __future__ import unicode_literals

from django.db import migrations
                    

class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0046_permission_account_permission_name'),
    ]               

    operations = [
        migrations.RunSQL("UPDATE dataentry_permission SET min_level = 'COUNTRY' where permission_group = 'STATIONS' and action = 'ADD';"),
        migrations.RunSQL("UPDATE dataentry_permission SET min_level = 'STATION' where permission_group = 'STATIONS' and action in ('VIEW', 'EDIT');"),
	    migrations.RunSQL("DELETE FROM dataentry_permission where permission_group = 'STATIONS' and action = 'DELETE';"),
    ]
