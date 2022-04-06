# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-03-24 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0219_empowerment_vdf_number'),
        ('budget', '0009_auto_20220209_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherbudgetitemcost',
            name='work_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation'),
        ),
        migrations.AddField(
            model_name='staffbudgetitem',
            name='work_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation'),
        ),
        migrations.RemoveField(
            model_name='borderstationbudgetcalculation',
            name='travel_plus_other',
        ),
        migrations.RemoveField(
            model_name='borderstationbudgetcalculation',
            name='awareness_contact_cards_boolean_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='travel_chair_with_bike',
            new_name='travel_chair',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='travel_chair_with_bike_amount',
            new_name='travel_chair_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_number_of_intercepts_last_month',
            new_name='number_of_intercepts_last_month',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_number_of_intercepts_last_month_multiplier',
            new_name='number_of_intercepts_last_month_multiplier',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_number_of_intercepts_last_month_adder',
            new_name='number_of_intercepts_last_month_adder',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_number_of_meetings_per_month',
            new_name='number_of_meetings_per_month',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_number_of_meetings_per_month_multiplier',
            new_name='number_of_meetings_per_month_multiplier',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_booth',
            new_name='booth',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_booth_amount',
            new_name='booth_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_office',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='administration_office_amount',
            new_name='office_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='food_and_gas_number_of_intercepted_girls',
            new_name='number_of_intercepted_pvs',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='food_and_gas_number_of_intercepted_girls_multiplier_before',
            new_name='food_per_pv_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='food_and_gas_number_of_intercepted_girls_multiplier_after',
            new_name='number_of_pv_days',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='food_and_gas_limbo_girls_multiplier',
            new_name='limbo_girls_multiplier',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='awareness_contact_cards',
            new_name='contact_cards',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='awareness_contact_cards_amount',
            new_name='contact_cards_amount',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='awareness_awareness_party_boolean',
            new_name='awareness_party_boolean',
        ),
        migrations.RenameField(
            model_name='borderstationbudgetcalculation',
            old_name='awareness_awareness_party',
            new_name='awareness_party',
        ),
        
    ]
