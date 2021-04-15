# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-09-03 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0150_pendingmatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_case_number',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_entry',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_exit',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_lj_entry',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_lj_exit',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_lj_transit',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='immigration_transit',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_connection_host_unclear',
            field=models.BooleanField(default=False, verbose_name='Connection to host/suspect limited or unclear'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_doesnt_have_required_visa',
            field=models.BooleanField(default=False, verbose_name="Doesn't have required visa/docs"),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_doesnt_speak_english',
            field=models.BooleanField(default=False, verbose_name="Doesn't speak English"),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_non_relative_paid_flight',
            field=models.BooleanField(default=False, verbose_name='Non-relative paid for flight'),
        ),
        migrations.AddField(
            model_name='irfcommon',
            name='vulnerability_paid_flight_in_cash',
            field=models.BooleanField(default=False, verbose_name='Non-relative paid for flight'),
        ),
        
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Young looking woman' else profile || ';Young looking woman' end) "\
                          "where (young_woman_going_to_mining_town = true or group_young_women_kids = true) and "\
                          "profile not like '%Young looking woman%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Young looking' else profile || ';Young looking' end) "\
                          "where noticed_young_looking = true and "\
                          "profile not like '%Young looking%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Child(ren)' else profile || ';Child(ren)' end) "\
                          "where (who_in_group_pv_under_14=true or undocumented_children_in_group=true or who_in_group_children_with_parents=true "\
                            "or who_in_group_children_with_other_adults=true or who_in_group_children_non_relative=true "
                            "or who_in_group_children_alone=true or who_in_group_with_kids=true or who_in_group_kids_under_5=true "\
                            "or profile_children=true) and "\
                          "profile not like '%Child(ren)%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Different ethnicities' else profile || ';Different ethnicities' end) "\
                          "where different_ethnicities = true and "\
                          "profile not like '%Different ethnicities%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Girl from Nepal/Bangladesh' else profile || ';Girl from Nepal/Bangladesh' end) "\
                          "where girl_from_nepal_bangladesh = true and "\
                          "profile not like '%Different ethnicities%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Albino' else profile || ';Albino' end) "\
                          "where who_in_group_albino = true and "\
                          "profile not like '%Albino%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Escaping an exploitative situation' else profile || ';Escaping an exploitative situation' end) "\
                          "where exploitative_situation = true and "\
                          "profile not like '%Escaping an exploitative situation%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Runaway' else profile || ';Runaway' end) "\
                          "where (where_runaway = true or running_away_over_18=true or running_away_under_18=true) and "\
                          "profile not like '%Runaway%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Drug withdrawal' else profile || ';Drug withdrawal' end) "\
                          "where appearance_drug_withdrawl = true and "\
                          "profile not like '%Drug withdrawal%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Signs of abuse' else profile || ';Signs of abuse' end) "\
                          "where appearance_abuse = true and "\
                          "profile not like '%Signs of abuse%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Disorientated' else profile || ';Disorientated' end) "\
                          "where appearance_disorientated = true and "\
                          "profile not like '%Disorientated%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Impoverished' else profile || ';Impoverished' end) "\
                          "where appearance_impoverished = true and "\
                          "profile not like '%Impoverished%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Revealing clothing' else profile || ';Revealing clothing' end) "\
                          "where appearance_revealing_clothing = true and "\
                          "profile not like '%Revealing clothing%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'With chaperone' else profile || ';With chaperone' end) "\
                          "where appearance_with_chaperone = true and "\
                          "profile not like '%With chaperone%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'New clothes' else profile || ';New clothes' end) "\
                          "where noticed_new_clothes = true and "\
                          "profile not like '%New clothes%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Dirty clothes' else profile || ';Dirty clothes' end) "\
                          "where noticed_dirty_clothes = true and "\
                          "profile not like '%Dirty clothes%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Village dress' else profile || ';Village dress' end) "\
                          "where noticed_village_dress = true and "\
                          "profile not like '%Village dress%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Foreign looking' else profile || ';Foreign looking' end) "\
                          "where noticed_foreign_looking = true and "\
                          "profile not like '%Foreign looking%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Typical village look' else profile || ';Typical village look' end) "\
                          "where noticed_typical_village_look = true and "\
                          "profile not like '%Typical village look%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Caste difference' else profile || ';Caste difference' end) "\
                          "where noticed_caste_difference = true and "\
                          "profile not like '%Caste difference%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then 'Migrant' else profile || ';Migrant' end) "\
                          "where profile_migrant = true and "\
                          "profile not like '%Migrant%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set profile = (case when profile='' then profile_other else profile || ';' || profile_other end) "\
                          "where profile_other != '' and "\
                          "profile not like '%' || profile_other || '%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
       
       
       
       
        migrations.RunSQL("update dataentry_irfcommon set vulnerability_family_unwilling=under_18_family_unwilling  and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set study_doesnt_know_school_details=true "\
                          "where (study_doesnt_know_school_details = true or no_enrollment_docs = true or doesnt_know_school_name = true or no_school_phone = true)  and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Massage Parlor' else industry || ';Massage Parlor' end) "\
                          "where employment_massage_parlor = true and "\
                          "industry not like '%Massage Parlor%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Farm work' else industry || ';Farm work' end) "\
                          "where seasonal_farm_work = true and "\
                          "industry not like '%Farm work%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Unregistered Mine' else industry || ';Unregistered Mine' end) "\
                          "where unregistered_mine = true and "\
                          "industry not like '%Unregistered Mine%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Salon' else industry || ';Salon' end) "\
                          "where employment_salon = true and "\
                          "industry not like '%Salon%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Domestic work' else industry || ';Domestic work' end) "\
                          "where (going_abroad_domestic_work = true or visa_for_domestic_work = true ) and "\
                          "industry not like '%Domestic work%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Plantation work' else industry || ';Plantation work' end) "\
                          "where going_plantation_work = true and "\
                          "industry not like '%Plantation work%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then 'Dance' else industry || ';Dance' end) "\
                          "where employment_dance = true and "\
                          "industry not like '%Dance%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),  
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then purpose_for_going_other else industry || ';' || purpose_for_going_other end) "\
                          "where purpose_for_going_other != '' and "\
                          "industry not like '%' || purpose_for_going_other || '%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set industry=("\
                          "case when industry='' then work_sector_other else industry || ';' || work_sector_other end) "\
                          "where work_sector_other != '' and "\
                          "industry not like '%' || work_sector_other || '%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'India' else where_going_destination || ';India' end) "\
                          "where where_going_india = true and "\
                          "where_going_destination not like '%India%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Middle East' else where_going_destination || ';Middle East' end) "\
                          "where (where_going_middle_east = true or destination_middle_east = true) and "\
                          "where_going_destination not like '%Middle East%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Thailand' else where_going_destination || ';Thailand' end) "\
                          "where thailand_destination != '' and "\
                          "where_going_destination not like '%Thailand%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Malaysia' else where_going_destination || ';Malaysia' end) "\
                          "where malaysia_destination != '' and "\
                          "where_going_destination not like '%Malaysia%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Lake Volta region' else where_going_destination || ';Lake Volta region' end) "\
                          "where destination_lake_volta_region = true and "\
                          "where_going_destination not like '%Lake Volta region%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Lesotho' else where_going_destination || ';Lesotho' end) "\
                          "where destination_lesotho = true and "\
                          "where_going_destination not like '%Lesotho%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Mozambique' else where_going_destination || ';Mozambique' end) "\
                          "where destination_mozambique = true and "\
                          "where_going_destination not like '%Mozambique%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
        migrations.RunSQL("update dataentry_irfcommon set where_going_destination=("\
                          "case when where_going_destination='' then 'Nigeria' else where_going_destination || ';Nigeria' end) "\
                          "where destination_nigeria = true and "\
                          "where_going_destination not like '%Nigeria%' and "\
                          "station_id in (select s.id from dataentry_borderstation s, dataentry_country c where s.operating_country_id = c.id and "\
                          "c.name in ('Benin','South Africa','Namibia'))"),
    ]
