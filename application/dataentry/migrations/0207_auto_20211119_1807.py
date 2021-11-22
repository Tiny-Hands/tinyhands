# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-19 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0206_personmatch_match_results'),
    ]

    operations = [
        migrations.RunSQL("delete from dataentry_userlocationpermission where permission_id in "\
                            "(select id from dataentry_permission where permission_group in ('FORMS','VIF'))"),
        migrations.RunSQL("delete from dataentry_permission where permission_group in ('FORMS','VIF')"),
    ]
