# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-11-01 13:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0118_auto_20191028_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntercepteeCambodia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='', upload_to='interceptee_photos')),
                ('anonymized_photo', models.CharField(max_length=126, null=True)),
                ('kind', models.CharField(choices=[('v', 'Victim'), ('t', 'Trafficker'), ('u', 'Unknown')], max_length=4)),
                ('relation_to', models.CharField(blank=True, max_length=255)),
                ('trafficker_taken_into_custody', models.BooleanField(default=False, verbose_name='taken_into_custody')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IrfAttachmentCambodia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=126, null=True)),
                ('attachment', models.FileField(upload_to='scanned_irf_forms', verbose_name='Attach scanned copy of form (pdf or image)')),
                ('private_card', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IrfCambodia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('irf_number', models.CharField(max_length=20, unique=True, verbose_name='IRF #:')),
                ('number_of_victims', models.PositiveIntegerField(blank=True, null=True, verbose_name='# of victims:')),
                ('location', models.CharField(max_length=255, verbose_name='Location:')),
                ('date_time_of_interception', models.DateTimeField(verbose_name='Date/Time:')),
                ('number_of_traffickers', models.PositiveIntegerField(blank=True, null=True, verbose_name='# of traffickers')),
                ('staff_name', models.CharField(max_length=255, verbose_name='Staff Name:')),
                ('drugged_or_drowsy', models.BooleanField(default=False, verbose_name='Girl appears drugged or drowsy')),
                ('who_in_group_husbandwife', models.BooleanField(default=False, verbose_name='Husband / Wife')),
                ('married_in_past_2_weeks', models.BooleanField(default=False, verbose_name='Married in the past 2 weeks')),
                ('married_in_past_2_8_weeks', models.BooleanField(default=False, verbose_name='Married within the past 2-8 weeks')),
                ('caught_in_lie', models.BooleanField(default=False, verbose_name='Caught in a lie or contradiction')),
                ('other_red_flag', models.CharField(blank=True, max_length=255)),
                ('where_going_destination', models.CharField(blank=True, max_length=126, verbose_name='Location:')),
                ('where_going_job', models.BooleanField(default=False, verbose_name='Job')),
                ('passport_with_broker', models.BooleanField(default=False, verbose_name='Passport is with a broker')),
                ('job_too_good_to_be_true', models.BooleanField(default=False, verbose_name='Job is too good to be true')),
                ('not_real_job', models.BooleanField(default=False, verbose_name='Not a real job')),
                ('couldnt_confirm_job', models.BooleanField(default=False, verbose_name='Could not confirm job')),
                ('where_going_study', models.BooleanField(default=False, verbose_name='Study')),
                ('no_enrollment_docs', models.BooleanField(default=False, verbose_name='No documentation of enrollment')),
                ('doesnt_know_school_name', models.BooleanField(default=False, verbose_name="Does not Know School's Name and location")),
                ('no_school_phone', models.BooleanField(default=False, verbose_name='No phone number for School')),
                ('not_enrolled_in_school', models.BooleanField(default=False, verbose_name='Not enrolled in school')),
                ('where_runaway', models.BooleanField(default=False, verbose_name='Runaway')),
                ('running_away_over_18', models.BooleanField(default=False, verbose_name='Running away from home (18 years or older)')),
                ('running_away_under_18', models.BooleanField(default=False, verbose_name='Running away from home (under 18 years old)')),
                ('reluctant_family_info', models.BooleanField(default=False, verbose_name='Reluctant to give family info')),
                ('refuses_family_info', models.BooleanField(default=False, verbose_name='Will not give family info')),
                ('under_18_cant_contact_family', models.BooleanField(default=False, verbose_name='No family contact established')),
                ('under_18_family_doesnt_know', models.BooleanField(default=False, verbose_name="Family doesn't know she is going to India")),
                ('under_18_family_unwilling', models.BooleanField(default=False, verbose_name='Family unwilling to let her go')),
                ('talked_to_family_member', models.CharField(blank=True, max_length=127)),
                ('reported_total_red_flags', models.IntegerField(blank=True, null=True, verbose_name='Reported Total Red Flag Points:')),
                ('computed_total_red_flags', models.IntegerField(blank=True, null=True, verbose_name='Computed Total Red Flag Points:')),
                ('who_noticed', models.CharField(max_length=127, null=True)),
                ('staff_who_noticed', models.CharField(blank=True, max_length=255, verbose_name='Staff who noticed:')),
                ('type_of_intercept', models.CharField(max_length=127, null=True)),
                ('how_sure_was_trafficking', models.IntegerField(choices=[(1, '1 - Not at all sure'), (2, '2 - Unsure but suspects it'), (3, '3 - Somewhat sure'), (4, '4 - Very sure'), (5, '5 - Absolutely sure')], null=True, verbose_name='How sure are you that it was trafficking case?')),
                ('convinced_by_staff', models.CharField(blank=True, max_length=127)),
                ('convinced_by_family', models.CharField(blank=True, max_length=127)),
                ('convinced_by_police', models.CharField(blank=True, max_length=127)),
                ('evidence_categorization', models.CharField(max_length=127, null=True)),
                ('reason_for_intercept', models.TextField(blank=True, verbose_name='Primary reason for intercept')),
                ('has_signature', models.BooleanField(default=False, verbose_name='Scanned form has signature?')),
                ('logbook_received', models.DateField(null=True)),
                ('logbook_incomplete_questions', models.CharField(blank=True, max_length=127)),
                ('logbook_incomplete_sections', models.CharField(blank=True, max_length=127)),
                ('logbook_information_complete', models.DateField(null=True)),
                ('logbook_notes', models.TextField(blank=True, verbose_name='Logbook Notes')),
                ('logbook_submitted', models.DateField(null=True)),
                ('logbook_first_verification', models.CharField(blank=True, max_length=127)),
                ('logbook_first_reason', models.TextField(blank=True, verbose_name='First Reason')),
                ('logbook_followup_call', models.CharField(blank=True, max_length=127)),
                ('logbook_first_verification_date', models.DateField(null=True)),
                ('logbook_leadership_review', models.CharField(blank=True, max_length=127)),
                ('logbook_second_verification', models.CharField(blank=True, max_length=127)),
                ('logbook_second_reason', models.TextField(blank=True, verbose_name='Second Reason')),
                ('logbook_second_verification_date', models.DateField(null=True)),
                ('logbook_back_corrected', models.TextField(blank=True, verbose_name='Back Corrected')),
                ('who_in_group_alone', models.BooleanField(default=False, verbose_name='Alone')),
                ('who_in_group_relative', models.BooleanField(default=False, verbose_name='Own brother, sister / relative')),
                ('who_in_group_broker', models.BooleanField(default=False, verbose_name='Broker/Other Person')),
                ('meeting_someone_across_border', models.BooleanField(default=False, verbose_name='Is meeting a someone just across border')),
                ('meeting_someone_they_dont_know', models.BooleanField(default=False, verbose_name="Supposed to meet someone they don't know")),
                ('crossing_border_separately', models.BooleanField(default=False, verbose_name='Someone who is crossing border separately')),
                ('agent_sent_them_on', models.BooleanField(default=False, verbose_name='An agent who sent them on')),
                ('relationship_married_two_months', models.BooleanField(default=False, verbose_name='During the past 2 months')),
                ('different_ethnicities', models.BooleanField(default=False, verbose_name='Appear to be of different ethnicities')),
                ('thailand_destination', models.CharField(blank=True, max_length=127)),
                ('malaysia_destination', models.CharField(blank=True, max_length=127)),
                ('where_going_other', models.CharField(blank=True, max_length=127)),
                ('work_sector_agriculture', models.BooleanField(default=False, verbose_name='Agriculture')),
                ('work_sector_construction', models.BooleanField(default=False, verbose_name='Construction')),
                ('work_sector_domestic_service', models.BooleanField(default=False, verbose_name='Domestic Services')),
                ('work_sector_dont_know', models.BooleanField(default=False, verbose_name="Don't know")),
                ('work_sector_factory', models.BooleanField(default=False, verbose_name='Factory')),
                ('work_sector_fishing', models.BooleanField(default=False, verbose_name='Fishing')),
                ('work_sector_hospitality', models.BooleanField(default=False, verbose_name='Hospitality')),
                ('work_sector_logging', models.BooleanField(default=False, verbose_name='Logging')),
                ('work_sector_other', models.CharField(blank=True, max_length=127)),
                ('no_company_phone', models.BooleanField(default=False, verbose_name='No company phone number')),
                ('job_confirmed', models.BooleanField(default=False, verbose_name='job confirmed')),
                ('valid_id_or_enrollment_documents', models.BooleanField(default=False, verbose_name='Valid ID card or enrollment documents')),
                ('enrollment_confirmed', models.BooleanField(default=False, verbose_name='Enrollment confirmed')),
                ('purpose_for_going_other', models.CharField(blank=True, max_length=127)),
                ('took_out_loan', models.CharField(blank=True, max_length=127)),
                ('recruited_broker', models.BooleanField(default=False, verbose_name='Broker/Agent')),
                ('how_recruited_broker_approached', models.BooleanField(default=False, verbose_name='Broker approached them')),
                ('met_broker_through_advertisement', models.BooleanField(default=False, verbose_name='Through advertisment')),
                ('met_broker_online', models.CharField(blank=True, max_length=127)),
                ('how_recruited_broker_other', models.CharField(blank=True, max_length=127)),
                ('broker_company', models.CharField(blank=True, max_length=127)),
                ('unwilling_to_give_info_about_broker', models.BooleanField(default=False, verbose_name='unwilling to give information about them')),
                ('initial_signs', models.TextField(blank=True, verbose_name='Initial Signs')),
                ('case_notes', models.TextField(blank=True, verbose_name='Case Notes')),
                ('broker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person')),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='irfcambodia_entered_by', to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
                ('where_going_doesnt_know', models.BooleanField(default=False, verbose_name="Don't know where going")),
                ('expected_earning', models.CharField(blank=True, max_length=127)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='irfattachmentcambodia',
            name='interception_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.IrfCambodia'),
        ),
        migrations.AddField(
            model_name='intercepteecambodia',
            name='interception_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interceptees', to='dataentry.IrfCambodia'),
        ),
        migrations.AddField(
            model_name='intercepteecambodia',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person'),
        ),
    ]
