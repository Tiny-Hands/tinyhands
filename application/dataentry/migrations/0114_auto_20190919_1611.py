# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-09-19 16:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0113_auto_20190909_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonFormCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_detail', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Person')),
            ],
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxbangladesh',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxbenin',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxghana',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxindia',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxkenya',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxmalawi',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxnepal',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxosi',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxsierraleone',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxsouthafrica',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxtanzania',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_agent',
            field=models.BooleanField(default=False, verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_broker',
            field=models.BooleanField(default=False, verbose_name='Broker'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_companion',
            field=models.BooleanField(default=False, verbose_name='Companion'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_complainant',
            field=models.BooleanField(default=False, verbose_name='Complainant'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_host',
            field=models.BooleanField(default=False, verbose_name='Host'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_id_facilitator',
            field=models.BooleanField(default=False, verbose_name='ID Facilitator'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_other',
            field=models.CharField(max_length=126, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='personboxuganda',
            name='role_witness',
            field=models.BooleanField(default=False, verbose_name='Witness'),
        ),
    ]
