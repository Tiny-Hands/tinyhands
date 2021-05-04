# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-04-27 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_border_stations', '0003_auto_20200721_1709'),
        ('dataentry', '0180_auto_20210420_1903'),
    ]

    operations = [
        migrations.RunSQL("select year_month, location_id, "\
                          "sum(intercepts) as intercepts, "\
                          "sum(intercepts_evidence) as intercepts_evidence, "\
                          "sum(intercepts_high_risk) as intercepts_high_risk, "\
                          "sum(intercepts_invalid) as intercepts_invalid, "\
                          "sum(arrests) as arrests "\
                          "into tmp_locationstatistics "\
                          "from dataentry_locationstatistics "\
                          "group by year_month, location_id"),
        migrations.RunSQL("delete from dataentry_locationstatistics"),
        migrations.RunSQL("insert into dataentry_locationstatistics (year_month, location_id, intercepts, intercepts_evidence, intercepts_high_risk, intercepts_invalid, arrests, modified_date) "\
                          "(select year_month, location_id, intercepts, intercepts_evidence, intercepts_high_risk, intercepts_invalid, arrests, CURRENT_TIMESTAMP from tmp_locationstatistics)"),
    ]