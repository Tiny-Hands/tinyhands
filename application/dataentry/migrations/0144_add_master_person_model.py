# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-05-20 14:07
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0143_auto_20200513_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasterPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'm'), ('F', 'f')], max_length=4)),
                ('birthdate', models.DateField(null=True)),
                ('estimated_birthdate', models.BooleanField(default=False, verbose_name='Estimated birthdate')),
                ('nationality', models.CharField(blank=True, default='', max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('address_notes', models.TextField(blank=True, verbose_name='Address Notes')),
                ('address_verified', models.BooleanField(default=False, verbose_name='Address Verified')),
                ('address_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.AddressType')),
                ('master_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.MasterPerson')),
            ],
        ),
        migrations.CreateModel(
            name='PersonDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_location', models.FileField(upload_to='person_documents', verbose_name='Attach scanned copy of form (pdf or image)')),
                ('document_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.DocumentType')),
                ('master_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.MasterPerson')),
            ],
        ),
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255)),
                ('phone_verified', models.BooleanField(default=False, verbose_name='Phone Verified')),
                ('master_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.MasterPerson')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='address_verified',
            field=models.BooleanField(default=False, verbose_name='Address Verified'),
        ),
        migrations.AddField(
            model_name='person',
            name='master_set_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='master_set_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='master_set_notes',
            field=models.TextField(blank=True, verbose_name='Match Notes'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_verified',
            field=models.BooleanField(default=False, verbose_name='Phone Verified'),
        ),
        migrations.AddField(
            model_name='personphone',
            name='phone_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.PhoneType'),
        ),
        migrations.AddField(
            model_name='person',
            name='address_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.AddressType'),
        ),
        migrations.RunSQL("insert into dataentry_masterperson (id, gender, estimated_birthdate, nationality)  values(0, 'M', false, '')"),
        migrations.AddField(
            model_name='person',
            name='master_person',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dataentry.MasterPerson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataentry.PhoneType'),
        ),
    ]
