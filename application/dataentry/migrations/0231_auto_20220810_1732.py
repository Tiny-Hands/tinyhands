# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-10 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0230_auto_20220702_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('form_version', models.CharField(max_length=126, null=True)),
                ('incident_number', models.CharField(max_length=20, unique=True, verbose_name='Incident #:')),
                ('incident_date', models.DateField('Incident date')),
                ('summary', models.TextField(blank=True)),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incident_entered_by', to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='other_contact_name',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='other_contact_phone',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='social_media_platform',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='whatsApp',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='broker_paid_amount',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='broker_paid_currency',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_lasted_days',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_began_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_began_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_lasted_years',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='job_promised',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='job_promised_amount',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='job_promised_currency',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_expenses_paid_how',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_left_home_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_paid_broker_amount',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_paid_broker_currency',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_recruited_agency',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_recruited_broker',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_recruited_how',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_recruited_no',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_thinks_they_were_trafficked',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='pv_traveled_how',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='recruited_agency_name',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='recruited_broker_names',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='victim_testimony',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='other_shelter',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='overnight_lodging',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='share_gospel_connect_to_local_church',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_explain',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse_suspects',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='vdfcommon',
            name='exploit_physical_abuse_lasted_days',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_debt_bondage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_forced_labor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_physical_abuse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_prostitution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vdfcommon',
            name='exploit_sexual_abuse',
            field=models.BooleanField(default=False),
        ),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('PVF','VIEW','STATION',1)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('PVF','VIEW PI','STATION',2)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('PVF','EDIT','STATION',3)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('PVF','ADD','STATION',4)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('PVF','DELETE','STATION',5)"),
        migrations.RunSQL("insert into dataentry_incident (status, station_id, form_entered_by_id, incident_number, incident_date, summary, date_time_entered_into_system, date_time_last_updated) "\
                          "select 'approved', station_id, form_entered_by_id, irf_number as incident_number, date_of_interception, '', date_time_entered_into_system, date_time_last_updated from dataentry_irfcommon"),
    ]
