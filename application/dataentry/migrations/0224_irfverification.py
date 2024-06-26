# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-30 12:23
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0223_auto_20220512_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='IrfVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_type', models.IntegerField(verbose_name=[(1, 'Initial Verification'), (2, 'Tie Break'), (3, 'Tie Break Review'), (4, 'Override')])),
                ('followup_call', models.CharField(blank=True, max_length=127)),
                ('followup_details', models.TextField(blank=True, verbose_name='followup details')),
                ('evidence_categorization', models.CharField(max_length=127)),
                ('reason', models.TextField(blank=True, verbose_name='reason')),
                ('verified_date', models.DateField()),
                ('verifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('interception_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.IrfCommon')),
            ],
            options={
                'abstract': False,
            },
        ),
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
                                "where name in ('Nepal')))"
        ),
        migrations.RunSQL(
            'insert into dataentry_irfverification (interception_record_id, verification_type, followup_call, followup_details, evidence_categorization,'\
                    'reason, verified_date, verifier_id) '\
                "select irf.id, 2, '', '', irf.logbook_second_verification, irf.logbook_second_reason, "\
                        'irf.logbook_second_verification_date, acc.id '\
                'from dataentry_irfcommon as irf '\
                    "left outer join accounts_account as acc on irf.logbook_second_verification_name = acc.first_name || ' ' || acc.last_name " \
                'where irf.logbook_second_verification_date is not null and irf.station_id in ('\
                        'select id from dataentry_borderstation '\
                        'where operating_country_id in ('\
                                'select id from dataentry_country '\
                                "where name in ('Nepal')))"
        ),
        migrations.RunSQL(
            'update dataentry_irfcommon '\
            "set status = 'approved'"
            "where status = 'first-verification'   and station_id in ("
                    'select id from dataentry_borderstation '\
                    'where operating_country_id in ('\
                            'select id from dataentry_country '\
                            "where name in ('Nepal')))"
        ),
        migrations.RunSQL(
            'update dataentry_irfcommon '\
            "set status = 'verified'"
            "where status = 'second-verification'   and station_id in ("
                    'select id from dataentry_borderstation '\
                    'where operating_country_id in ('\
                            'select id from dataentry_country '\
                            "where name in ('Nepal')))"
        ),
    ]
