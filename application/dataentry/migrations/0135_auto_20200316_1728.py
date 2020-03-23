# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-03-16 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0134_auto_20200311_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercepteecommon',
            name='not_physically_present',
            field=models.BooleanField(default=False, verbose_name='Not physically present'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_job',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_led_other_country',
            field=models.BooleanField(default=False, verbose_name='Led to other country without their knowledge'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_no_address_phone',
            field=models.BooleanField(default=False, verbose_name='No address / phone number (of job)'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_normal_pay',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_owes_debt',
            field=models.BooleanField(default=False, verbose_name='Owes debt to person who recruited/paid travel'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_promised_double',
            field=models.BooleanField(default=False, verbose_name='Promised pay more than double normal pay'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_promised_higher',
            field=models.BooleanField(default=False, verbose_name='Promised pay a little higher than normal pay'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_promised_pay',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='control_traveling_because_of_threat',
            field=models.BooleanField(default=False, verbose_name='Traveling because of a threat'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='convinced_family_phone',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='industry',
            field=models.CharField(blank=True, max_length=126, verbose_name='Industry'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='profile_children',
            field=models.BooleanField(default=False, verbose_name='Child(ren)'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='profile_migrant',
            field=models.BooleanField(default=False, verbose_name='Migrant'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='profile_other',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='signs_confirmed_deception',
            field=models.BooleanField(default=False, verbose_name='Called place and confirmed deception'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='signs_forged_false_documentation',
            field=models.BooleanField(default=False, verbose_name='Forged or falsified documents'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='signs_other',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='signs_treatment',
            field=models.BooleanField(default=False, verbose_name='Treatment - no documentation / knowledge'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_insufficient_resource',
            field=models.BooleanField(default=False, verbose_name='insufficient resources_to live/get home'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_minor_without_guardian',
            field=models.BooleanField(default=False, verbose_name='Minor unaccompanied by guardian'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_family_unwilling',
            field=models.BooleanField(default=False, verbose_name='Family unwilling to let them go'),
        ),
        migrations.RunSQL("update dataentry_irfcommon set vulnerability_family_unwilling=under_18_family_unwilling "\
                          "where station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and c.name='India Network')"),
        migrations.RunSQL("update dataentry_irfcommon set vulnerability_minor_without_guardian=true "\
                          "where (who_in_group_children_with_other_adults = true or who_in_group_children_alone = true) and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and c.name='India Network')"),
        migrations.RunSQL("update dataentry_irfcommon set control_no_address_phone=true "\
                          "where (no_address_at_destination = true or no_company_phone = true) and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and c.name='India Network')"),
        migrations.RunSQL("update dataentry_irfcommon set study_doesnt_know_school_details=true "\
                          "where (study_doesnt_know_school_details = true or no_enrollment_docs = true or doesnt_know_school_name = true or no_school_phone = true) and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and c.name='India Network')"),
        migrations.RunSQL("update dataentry_irfcommon set industry='Domestic work' "\
                          "where work_sector_domestic_service = true and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and c.name='India Network')"),
    ]
