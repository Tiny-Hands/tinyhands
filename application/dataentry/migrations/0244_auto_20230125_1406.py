# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-01-25 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0243_auto_20230124_1530'),
    ]

    operations = [
        migrations.RunSQL(
            'insert into dataentry_irfverification (interception_record_id, verification_type, followup_call, followup_details, evidence_categorization,'\
                    'reason, verified_date, verifier_id) '\
                "select irf.id, 1, irf.logbook_followup_call, '', irf.logbook_first_verification, irf.logbook_first_reason, "\
                        'irf.logbook_first_verification_date, acc.id '\
                'from dataentry_irfcommon as irf '
                    "left outer join accounts_account as acc on irf.logbook_first_verification_name = acc.first_name || ' ' || acc.last_name " \
                'where irf.logbook_first_verification_date is not null and irf.station_id in ('\
                        'select id from dataentry_borderstation '\
                        'where operating_country_id in ('\
                                'select id from dataentry_country '\
                                "where name in ('Burkina Faso')))"
        ),
        migrations.RunSQL(
            'insert into dataentry_irfverification (interception_record_id, verification_type, followup_call, followup_details, evidence_categorization,'\
                    'reason, verified_date, verifier_id) '\
                "select irf.id, 2, '', '', irf.verified_evidence_categorization, irf.logbook_second_reason, "\
                        'irf.verified_date, acc.id '\
                'from dataentry_irfcommon as irf '\
                    "left outer join accounts_account as acc on irf.logbook_second_verification_name = acc.first_name || ' ' || acc.last_name " \
                'where irf.verified_date is not null and irf.station_id in ('\
                        'select id from dataentry_borderstation '\
                        'where operating_country_id in ('\
                                'select id from dataentry_country '\
                                "where name in ('Burkina Faso')))"
        ),
        migrations.RunSQL(
            'update dataentry_irfcommon '\
            "set status = 'approved'"
            "where status = 'first-verification'   and station_id in ("
                    'select id from dataentry_borderstation '\
                    'where operating_country_id in ('\
                            'select id from dataentry_country '\
                            "where name in ('Burkina Faso')))"
        ),
        migrations.RunSQL(
            'update dataentry_irfcommon '\
            "set status = 'verified'"
            "where status = 'second-verification'   and station_id in ("
                    'select id from dataentry_borderstation '\
                    'where operating_country_id in ('\
                            'select id from dataentry_country '\
                            "where name in ('Burkina Faso')))"
        ),
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set profile = replace(profile, 'Escaping an exploitative situation', 'Recently enslaved') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set vulnerability_travel_met_recently = true "\
                            "where (vulnerability_group_missed_call = true or vulnerability_group_facebook = true or vulnerability_group_other_website != '') "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set case_notes = case_notes || '\n' || reason_for_intercept "\
                            "where reason_for_intercept != '' "\
                            "and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set where_going_destination = (case when where_going_destination='' "\
                                "then 'PV doesn\'\'t know' else where_going_destination || ';PV doesn\'\'t know' end) "\
                            "where vulnerability_where_going_doesnt_know = true and station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_person "\
                          "set arrested=null "\
                            "where arrested='No' and id in ("\
                                "select di.person_id "\
                                "from dataentry_intercepteecommon di "\
                                    "inner join dataentry_irfcommon dc1 on di.interception_record_id = dc1.id "\
                                    "inner join dataentry_borderstation db on dc1.station_id = db.id "\
                                    "inner join dataentry_country dc on db.operating_country_id = dc.id "\
                                "where dc.name in ('Burkina Faso'))"),
        
        # Country specific migration
        
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set profile = replace(profile, 'Illiterate', 'Uneducated') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set profile = replace(profile, 'Villager', 'Village look') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set industry = replace(industry, 'Rural work', 'Agriculture') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
        migrations.RunSQL("update dataentry_irfcommon "\
                          "set industry = replace(industry, 'Waitress', 'Restaurant') "\
                            "where station_id in ("\
                                "select dbs.id "\
                                "from dataentry_borderstation dbs "\
                                    "inner join dataentry_country dc on dc.id = dbs.operating_country_id "\
                                "where dc.name in ('Burkina Faso'))"),
    ]
