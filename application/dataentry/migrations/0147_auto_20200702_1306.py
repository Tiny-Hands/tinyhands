# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-07-02 13:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0146_auto_20200601_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterceptionCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_date', models.DateField()),
                ('interceptions', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RunSQL("insert into dataentry_region (id, name) values(1, 'Africa') "),
        migrations.RunSQL("insert into dataentry_region (id, name) values(2, 'Asia') "),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Region'),
            preserve_default=False,
        ),
        migrations.RunSQL("update dataentry_country set region_id=2 where name in ('Nepal','India','Bangladesh','Mongolia','India Network','Cambodia') "),
    ]
