# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0003_district_vdc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victiminterviewlocationbox',
            name='geolocation',
        ),
        migrations.DeleteModel(
            name='GeoCodeLocation',
        ),
        migrations.AddField(
            model_name='vdc',
            name='cannonical_name',
            field=models.ForeignKey(default=1, to='dataentry.VDC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='victiminterviewlocationbox',
            name='district_geocodelocation',
            field=models.ForeignKey(default=1, to='dataentry.District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='victiminterviewlocationbox',
            name='vdc_geocodelocation',
            field=models.ForeignKey(default=1, to='dataentry.VDC'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vdc',
            name='district',
            field=models.ForeignKey(to='dataentry.District'),
        ),
    ]
