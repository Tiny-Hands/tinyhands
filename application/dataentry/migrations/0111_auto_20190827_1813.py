# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-27 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0110_auto_20190830_1950'),
    ]

    operations = [

        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxbangladesh',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxbenin',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxghana',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxindia',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxkenya',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxmalawi',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxnepal',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxosi',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxsierraleone',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxsouthafrica',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxtanzania',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_broker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_companion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_complainant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_host',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_id_facilitator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_other',
            field=models.CharField(max_length=126, null=True),
        ),
        migrations.AddField(
            model_name='personboxuganda',
            name='role_witness',
            field=models.BooleanField(default=False),
        ),
        migrations.RunSQL("UPDATE dataentry_personboxbangladesh set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),
        
        migrations.RunSQL("UPDATE dataentry_personboxbenin set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxghana set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxindia set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxkenya set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxmalawi set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),


        migrations.RunSQL("UPDATE dataentry_personboxnepal set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxosi set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxsierraleone set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxsouthafrica set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxtanzania set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),

        migrations.RunSQL("UPDATE dataentry_personboxuganda set "\
                          "role_broker= (case when role='Broker' then true else false end), "\
                          "role_companion= (case when role='Companion' then true else false end), "\
                          "role_host= (case when role='Host' then true else false end), "\
                          "role_id_facilitator= (case when role='ID Facilitator' then true else false end), "\
                          "role_agent= (case when role='Agent' then true else false end), "\
                          "role_witness= (case when role='Witness' then true else false end), "\
                          "role_complainant= (case when role='Complainant' then true else false end), "\
                          "role_other= (case when role in ('','Broker','Companion','Host','ID Facilitator','Agent','Witness','Complainant') then null else role end)"),
    ]