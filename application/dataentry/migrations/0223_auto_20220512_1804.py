# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-12 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0222_borderstation_mdf_project'),
    ]

    operations = [
        migrations.RunSQL("update dataentry_borderstation "\
                          "set features=(case features when '' then 'hasMDF' else features || ';hasMDF' END)"),
        migrations.RunSQL("update dataentry_projectcategory "\
                          "set name='Transit Monitoring' where id=1"),
        migrations.RunSQL("update dataentry_projectcategory "\
                          "set name='National Office', sort_order=6 where id=3"),
        migrations.RunSQL("update dataentry_projectcategory "\
                          "set sort_order=7 where id=2"),
        migrations.RunSQL("insert into dataentry_projectcategory (name, sort_order) values('Investigations',2)"),
        migrations.RunSQL("insert into dataentry_projectcategory (name, sort_order) values('Safe Foreign Employment',3)"),
        migrations.RunSQL("insert into dataentry_projectcategory (name, sort_order) values('Police Training',4)"),
        migrations.RunSQL("insert into dataentry_projectcategory (name, sort_order) values('Empowerment',5)"),
    ]
