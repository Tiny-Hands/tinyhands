# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-29 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0084_auto_20190325_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='VdfAttachmentNepal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=126, null=True)),
                ('attachment', models.FileField(upload_to='vdf_attachments', verbose_name='Attach scanned copy of form (pdf or image)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VdfNepal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('vdf_number', models.CharField(max_length=20, unique=True, verbose_name='IRF #:')),
                ('staff_name', models.CharField(max_length=255, verbose_name='Staff Name:')),
                ('discharge_date', models.DateField(null=True, verbose_name='Incident date')),
                ('location', models.CharField(max_length=255, verbose_name='Location:')),
                ('occupation', models.CharField(max_length=126, null=True, verbose_name='Occupation')),
                ('guardian_name', models.CharField(max_length=126, null=True, verbose_name='Guardian Name')),
                ('guardian_phone', models.CharField(max_length=126, null=True, verbose_name='Guardian Phone')),
                ('guardian_know_destination', models.CharField(max_length=126, null=True, verbose_name='Did your guardian know you were traveling to intended destination?')),
                ('family_guardian_pressure', models.CharField(max_length=126, null=True, verbose_name="Did your family/guardian pressure you in any way to accept the broker's offer?")),
                ('try_to_send_overseas_again', models.CharField(max_length=126, null=True, verbose_name='If they attempted, do you think they will try to send you overseas again?')),
                ('feel_safe_with_guardian', models.CharField(max_length=126, null=True, verbose_name='Do you feel safe at home with your guardian?')),
                ('do_you_want_to_go_home', models.CharField(max_length=126, null=True, verbose_name='Do you want to go home?')),
                ('sexual_abuse', models.CharField(max_length=126, null=True, verbose_name='Sexual Abuse')),
                ('physical_abuse', models.CharField(max_length=126, null=True, verbose_name='Physical Abuse')),
                ('emotional_abuse', models.CharField(max_length=126, null=True, verbose_name='Emotional Abuse')),
                ('guardian_drink_alcohol', models.CharField(max_length=126, null=True, verbose_name='Does the Guardian drink alcohol?')),
                ('guardian_use_drugs', models.CharField(max_length=126, null=True, verbose_name='Does the Guardian use drugs?')),
                ('family_economic_situation', models.CharField(max_length=126, null=True, verbose_name='Economic Situation of Family')),
                ('express_suicidal_thoughts', models.CharField(max_length=126, null=True, verbose_name='Did the victim express any suicidal thoughts at any point?')),
                ('total_situational_alarms', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Situational Alarms')),
                ('station_recommendation_for_victim', models.CharField(max_length=126, null=True, verbose_name='What is the Border Station recommendation about where the victim should go?')),
                ('staff_share_gospel', models.CharField(max_length=126, null=True, verbose_name='Did the staff share the gospel with the victim?')),
                ('share_gospel_film', models.BooleanField(default=False, verbose_name='Film')),
                ('share_gospel_tract', models.BooleanField(default=False, verbose_name='Tract')),
                ('share_gospel_oral', models.BooleanField(default=False, verbose_name='Oral Preaching')),
                ('share_gospel_testimony', models.BooleanField(default=False, verbose_name='Shared Personal Testimony')),
                ('share_gospel_book', models.BooleanField(default=False, verbose_name='Message Book')),
                ('share_gospel_other', models.CharField(max_length=126, null=True, verbose_name='Other')),
                ('awareness_of_exploitation_before_interception', models.CharField(max_length=126, null=True, verbose_name='Before you were intercepted, were you aware that migrants going abroad are often deceived and end up in very exploitative situations?')),
                ('victim_heard_message_before', models.CharField(max_length=126, null=True, verbose_name='Had you ever heard the message before?')),
                ('what_victim_believes_now', models.CharField(max_length=126, null=True, verbose_name='What do you believe now?')),
                ('transit_staff_polite', models.PositiveIntegerField(blank=True, null=True, verbose_name='Transit Staff Polite and Respectful')),
                ('trafficking_awareness', models.PositiveIntegerField(blank=True, null=True, verbose_name='Trafficking Awareness')),
                ('shelter_staff_polite', models.PositiveIntegerField(blank=True, null=True, verbose_name='Shelter Staff Polite and Respectful')),
                ('shelter_accomodation', models.PositiveIntegerField(blank=True, null=True, verbose_name='Shelter Accomodations')),
                ('victim_still_at_shelter', models.CharField(max_length=126, null=True, verbose_name='Is victim still in the care of Border Station?')),
                ('date_victim_left', models.DateField(null=True, verbose_name='What date did victim leave the care of the Station')),
                ('someone_pick_up_victim', models.CharField(max_length=126, null=True, verbose_name='Did someone pick up victim from the station?')),
                ('who_victim_released', models.CharField(max_length=126, null=True, verbose_name='If yes, who was the victim released to?')),
                ('who_victim_released_name', models.CharField(max_length=126, null=True, verbose_name='Name of person whom the victim was released to')),
                ('who_victim_released_phone', models.CharField(max_length=126, null=True, verbose_name='Phone Number')),
                ('where_victim_sent', models.CharField(max_length=126, null=True, verbose_name='Where was the victim sent')),
                ('consent_to_use_information', models.CharField(max_length=126, null=True, verbose_name='I give consent to use any information I have shared throughout the duration of my time with the staff for operational and awareness purposes')),
                ('victim_signature', models.BooleanField(default=False, verbose_name='Victim Signature')),
                ('guardian_signature', models.BooleanField(default=False, verbose_name='Guardian Signature')),
                ('case_notes', models.TextField(blank=True, verbose_name='Case Notes')),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vdfnepal_entered_by', to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
                ('victim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='vdfattachmentnepal',
            name='vdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.VdfNepal'),
        ),
        migrations.RunSQL("INSERT INTO dataentry_permission (permission_group, action, min_level, account_permission_name) values ('VDF', 'VIEW','STATION',null);"),
        migrations.RunSQL("INSERT INTO dataentry_permission (permission_group, action, min_level, account_permission_name) values ('VDF', 'ADD','STATION',null);"),
        migrations.RunSQL("INSERT INTO dataentry_permission (permission_group, action, min_level, account_permission_name) values ('VDF', 'EDIT','STATION',null);"),
        migrations.RunSQL("INSERT INTO dataentry_permission (permission_group, action, min_level, account_permission_name) values ('VDF', 'DELETE','STATION',null);"),
    ]
