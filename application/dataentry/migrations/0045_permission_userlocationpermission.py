# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0044_interceptionalert_redflags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_group', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('min_level', models.CharField(default=b'STATION', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserLocationPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.Country')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Permission')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
            ],
        ),
    ]
