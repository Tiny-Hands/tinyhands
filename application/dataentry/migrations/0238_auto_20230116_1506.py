# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-16 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0237_auto_20230113_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='irfcommon',
            name='has_offical_signature',
            field=models.BooleanField(default=False, verbose_name='Has official signature'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='official_name',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='route',
            field=models.TextField(blank=True, verbose_name='Route'),
        ),
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set profile = replace(profile, 'Escaping an exploitative situation', 'Recently enslaved') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set vulnerability_travel_met_recently = true "\
                            "where (vulnerability_group_missed_call = true or vulnerability_group_facebook = true or vulnerability_group_other_website != '') "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set case_notes = case_notes || '\n' || reason_for_intercept "\
                            "where reason_for_intercept != '' "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set where_going_destination = (case when where_going_destination='' "\
                                "then 'PV doesn\'\'t know' else where_going_destination || ';PV doesn\'\'t know' end) "\
                            "where vulnerability_where_going_doesnt_know = true and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        migrations.RunSQL("update dataentry_person "\
                          "set arrested=null "\
                            "where arrested='No' and id in ("\
                                "select di.person_id "\
                                "from dataentry_intercepteecommon di "\
                                    "inner join dataentry_irfcommon dc1 on di.interception_record_id = dc1.id "\
                                    "inner join dataentry_borderstation db on dc1.station_id = db.id "\
                                    "inner join dataentry_country dc on db.operating_country_id = dc.id "\
                                "where dc.name in ('Namibia'))"),
                
        # Country specific migration
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set industry = replace(industry, 'Salon', 'Hair & beauty') "\
                            "where industry like '%Salon%' "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set industry = replace(industry, 'Hospitality', 'Hotel') "\
                            "where industry like '%Hospitality%' "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Namibia'))"),
        
        # missed data migrations for Kenya, South Africa and Ghana
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set profile = replace(profile, 'Escaping an exploitative situation', 'Recently enslaved') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Kenya','South Africa','Ghana'))"),
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set vulnerability_travel_met_recently = true "\
                            "where (vulnerability_group_missed_call = true or vulnerability_group_facebook = true or vulnerability_group_other_website != '') "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Kenya','South Africa','Ghana'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set case_notes = case_notes || '\n' || reason_for_intercept "\
                            "where reason_for_intercept != '' "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Kenya','South Africa','Ghana'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set where_going_destination = (case when where_going_destination='' "\
                                "then 'PV doesn\'\'t know' else where_going_destination || ';PV doesn\'\'t know' end) "\
                            "where vulnerability_where_going_doesnt_know = true and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Kenya','South Africa','Ghana'))"),
        migrations.RunSQL("update dataentry_person "\
                          "set arrested=null "\
                            "where arrested='No' and id in ("\
                                "select di.person_id "\
                                "from dataentry_intercepteecommon di "\
                                    "inner join dataentry_irfcommon dc1 on di.interception_record_id = dc1.id "\
                                    "inner join dataentry_borderstation db on dc1.station_id = db.id "\
                                    "inner join dataentry_country dc on db.operating_country_id = dc.id "\
                                "where dc.name in ('Kenya','South Africa','Ghana'))"),
    ]