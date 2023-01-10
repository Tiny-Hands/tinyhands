# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-28 19:50
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0234_auto_20220810_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(max_length=126, null=True)),
                ('source_title', models.CharField(blank=True, max_length=126)),
                ('interviewer_name', models.CharField(blank=True, max_length=126)),
                ('interview_date', models.DateField(default=None, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('persons_in_charge', models.CharField(max_length=126, null=True)),
                ('pvs_visited', models.CharField(max_length=126, null=True)),
                ('stay_how_long', models.CharField(max_length=126, null=True)),
                ('start_date', models.DateField(default=None, null=True)),
                ('attempt_hide', models.CharField(max_length=126, null=True)),
                ('attempt_explanation', models.CharField(max_length=126, null=True)),
                ('free_to_go', models.CharField(max_length=126, null=True)),
                ('free_to_go_explanation', models.CharField(max_length=126, null=True)),
                ('suspects_associative', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=126, null=True)),
                ('attachment', models.FileField(upload_to='lf_attachments', verbose_name='Attach scanned copy of form (pdf or image)')),
                ('private_card', models.BooleanField(default=True)),
                ('option', models.CharField(max_length=126, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluator_type', models.CharField(max_length=126, null=True)),
                ('evaluator_name', models.CharField(max_length=126, null=True)),
                ('evaluation', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('form_version', models.CharField(max_length=126, null=True)),
                ('lf_number', models.CharField(max_length=20, unique=True)),
                ('merged_place', models.CharField(max_length=126, null=True)),
                ('merged_place_detail', models.CharField(max_length=126, null=True)),
                ('merged_place_kind', models.CharField(max_length=126, null=True)),
                ('merged_address', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('merged_latitude', models.FloatField(null=True)),
                ('merged_longitude', models.FloatField(null=True)),
                ('merged_phone', models.CharField(max_length=126, null=True)),
                ('merged_name_signboard', models.CharField(max_length=126, null=True)),
                ('merged_location_in_town', models.CharField(max_length=126, null=True)),
                ('merged_color', models.CharField(max_length=126, null=True)),
                ('merged_number_of_levels', models.CharField(max_length=126, null=True)),
                ('merged_description', models.TextField(blank=True, verbose_name='Descriptive Features')),
                ('merged_nearby_landmarks', models.CharField(max_length=126, null=True)),
                ('evidence', models.TextField(blank=True)),
                ('how_facilitate', models.TextField(blank=True)),
                ('logbook_received', models.DateField(null=True)),
                ('logbook_incomplete_questions', models.CharField(blank=True, max_length=127)),
                ('logbook_incomplete_sections', models.CharField(blank=True, max_length=127)),
                ('logbook_information_complete', models.DateField(null=True)),
                ('logbook_notes', models.TextField(blank=True, verbose_name='Logbook Notes')),
                ('logbook_submitted', models.DateField(null=True)),
                ('associated_incidents', models.ManyToManyField(related_name='location_associated_incidents', to='dataentry.Incident')),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locationform_entered_by', to=settings.AUTH_USER_MODEL)),
                ('incidents', models.ManyToManyField(to='dataentry.Incident')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(max_length=126, null=True)),
                ('source_title', models.CharField(blank=True, max_length=126)),
                ('interviewer_name', models.CharField(blank=True, max_length=126)),
                ('interview_date', models.DateField(default=None, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('place', models.CharField(max_length=126, null=True)),
                ('place_detail', models.CharField(max_length=126, null=True)),
                ('place_kind', models.CharField(max_length=126, null=True)),
                ('address', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('phone', models.CharField(max_length=126, null=True)),
                ('name_signboard', models.CharField(max_length=126, null=True)),
                ('location_in_town', models.CharField(max_length=126, null=True)),
                ('color', models.CharField(max_length=126, null=True)),
                ('number_of_levels', models.CharField(max_length=126, null=True)),
                ('description', models.TextField(blank=True, verbose_name='Descriptive Features')),
                ('nearby_landmarks', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('lf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.LocationForm')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Suspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('form_version', models.CharField(max_length=126, null=True)),
                ('sf_number', models.CharField(max_length=20, unique=True)),
                ('merged_vehicle', models.CharField(max_length=126, null=True)),
                ('merged_plate_number', models.CharField(max_length=126, null=True)),
                ('logbook_received', models.DateField(null=True)),
                ('logbook_incomplete_questions', models.CharField(blank=True, max_length=127)),
                ('logbook_incomplete_sections', models.CharField(blank=True, max_length=127)),
                ('logbook_information_complete', models.DateField(null=True)),
                ('logbook_notes', models.TextField(blank=True, verbose_name='Logbook Notes')),
                ('logbook_submitted', models.DateField(null=True)),
                ('associated_incidents', models.ManyToManyField(related_name='associated_incidents', to='dataentry.Incident')),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suspect_entered_by', to=settings.AUTH_USER_MODEL)),
                ('incidents', models.ManyToManyField(to='dataentry.Incident')),
                ('merged_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuspectAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associated_pvs', models.CharField(max_length=126, null=True)),
                ('associated_suspects', models.CharField(max_length=126, null=True)),
                ('associated_locations', models.CharField(max_length=126, null=True)),
                ('narrative', models.TextField(blank=True, verbose_name='Narrative')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuspectAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=126, null=True)),
                ('attachment', models.FileField(upload_to='sf_attachments', verbose_name='Attach scanned copy of form (pdf or image)')),
                ('private_card', models.BooleanField(default=True)),
                ('option', models.CharField(max_length=126, null=True)),
                ('suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuspectEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluator_type', models.CharField(max_length=126, null=True)),
                ('evaluator_name', models.CharField(max_length=126, null=True)),
                ('evaluation', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuspectInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(max_length=126, null=True)),
                ('source_title', models.CharField(blank=True, max_length=126)),
                ('interviewer_name', models.CharField(blank=True, max_length=126)),
                ('interview_date', models.DateField(default=None, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('vehicle', models.CharField(max_length=126, null=True)),
                ('plate_number', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person')),
                ('suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuspectLegal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrested', models.CharField(max_length=126, null=True)),
                ('arrest_date', models.DateField(default=None, null=True)),
                ('police_case', models.CharField(max_length=126, null=True)),
                ('charge_sheet_date', models.DateField(default=None, null=True)),
                ('crimes_charged', models.TextField(blank=True, verbose_name='Crimes Charged')),
                ('pv_attempt', models.CharField(max_length=126, null=True)),
                ('pv_unable', models.CharField(max_length=126, null=True)),
                ('location_attempt', models.CharField(max_length=126, null=True)),
                ('location_unable', models.CharField(max_length=126, null=True)),
                ('location_last_address', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('location_last_latitude', models.FloatField(null=True)),
                ('location_last_longitude', models.FloatField(null=True)),
                ('location_last_address_notes', models.TextField(blank=True, verbose_name='Address Notes')),
                ('location_last_date', models.DateField(default=None, null=True)),
                ('police_attempt', models.CharField(max_length=126, null=True)),
                ('police_unable', models.CharField(max_length=126, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('suspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='locationevaluation',
            name='lf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.LocationForm'),
        ),
        migrations.AddField(
            model_name='locationattachment',
            name='lf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.LocationForm'),
        ),
        migrations.AddField(
            model_name='locationassociation',
            name='lf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.LocationForm'),
        ),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('SF','VIEW','PROJECT',1)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('SF','VIEW PI','PROJECT',2)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('SF','EDIT','PROJECT',3)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('SF','ADD','PROJECT',4)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('SF','DELETE','PROJECT',5)"),
        
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('LF','VIEW','PROJECT',1)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('LF','VIEW PI','PROJECT',2)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('LF','EDIT','PROJECT',3)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('LF','ADD','PROJECT',4)"),
        migrations.RunSQL("insert into dataentry_permission (permission_group, action, min_level, display_order)  values ('LF','DELETE','PROJECT',5)"),
    ]
