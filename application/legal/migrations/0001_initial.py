# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-09-04 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def migrate_legal_charge(apps, schema_editor):
    LegalCase = apps.get_model("dataentry", "LegalCase")
    LegalCaseTimeLine = apps.get_model("dataentry", "LegalCaseTimeLine")
    LegalCaseSuspect = apps.get_model("dataentry", "LegalCaseSuspect")
    LegalCaseVictim = apps.get_model("dataentry", "LegalCaseVictim")
    LegalCaseAttachment = apps.get_model("dataentry", "LegalCaseAttachment")
    
    SuspectInformation = apps.get_model("dataentry", "SuspectInformation")
    VdfCommon = apps.get_model("dataentry", "VdfCommon")
    Incident = apps.get_model("dataentry", "Incident")
    
    LegalCharge = apps.get_model("legal", "LegalCharge")
    CourtCase = apps.get_model("legal", "CourtCase")
    LegalChargeAttachment = apps.get_model("legal", "LegalChargeAttachment")
    LegalChargeSuspect = apps.get_model("legal", "LegalChargeSuspect")
    LegalChargeSuspectCharge = apps.get_model("legal", "LegalChargeSuspectCharge")
    LegalChargeTimeline = apps.get_model("legal", "LegalChargeTimeline")
    LegalChargeVictim = apps.get_model("legal", "LegalChargeVictim")
    
    source_map = {
        "By the information":"Informant",
        "Intercept":"Intercept",
        "By information":"Informant",
        "Police referral":"Police referral",
        "Information from HVC":"Informant",
        "Community referral":"Informant",
        "Informants":"Informant",
        "Foreign Employment":"Intercept",
        "":"Informant",
        "By Information":"Informant",
        "Investigations":"Investigations",
    }
    
    charge_map = {
        "":["Kidnapping"],   
        "Child labor":["Human Trafficking"],
        "Child Labor":["Human Trafficking"],
        "Child Marriage":["Human Trafficking"],
        "Defilement":["Sexual Assault"],
        "Domestic Violence":["Kidnapping"],
        "Foreign Employment":["Human Trafficking"],
        "Human Trafficking":["Human Trafficking"],
        "Human Trafficking & Rape":["Human Trafficking","Sexual Assault"],
        "Mis behave":["Kidnapping"],
        "Public Case":["Kidnapping"],
        "Rape":["Sexual Assault"],
        "Sexual Harassment":["Sexual Assault"],
        "Sodomy":["Sexual Assault"],
    };
    
    cases = LegalCase.objects.all()
    for case in cases:
        base_number = case.legal_case_number
        for idx in range(len(case.station.station_code), len(case.legal_case_number)):
            the_char = case.legal_case_number[idx]
            if (the_char < '0' or the_char > '9') and the_char != '_':
                base_number = case.legal_case_number[:idx]
                break
        try:
            incident = Incident.objects.get(incident_number = base_number)
        except:
            incident = Incident()
            incident.status = 'approved'
            incident.station = case.station
            if case.charge_sheet_date is not None:
                incident.incident_date = case.charge_sheet_date
            else:
                incident.incident_date = case.date_time_entered_into_system
            incident.incident_number = base_number
            incident.save()
            
        legal_charge = LegalCharge()
        legal_charge.status = case.status
        legal_charge.station = case.station
        legal_charge.form_version = 'Migrated'
        legal_charge.incident = incident
        legal_charge.legal_charge_number = case.legal_case_number;
        legal_charge.source = source_map[case.source]
        legal_charge.location = case.location
        legal_charge.charge_sheet_date = case.charge_sheet_date
        legal_charge.police_case = case.police_case
        legal_charge.human_trafficking = case.human_trafficking
        legal_charge.date_last_contacted = case.date_last_contacted
        legal_charge.missing_data_count = case.missing_data_count
        legal_charge.save()
        
        court_case = CourtCase()
        court_case.legal_charge = legal_charge
        court_case.sequence_number = 1     
        court_case.court_case = case.court_case
        theCharges = charge_map[case.case_type]
        sep = ''
        for theCharge in theCharges:
            court_case.charges += sep + theCharge
            sep = ';'
                
        court_case.specific_code_law = case.specific_code_law
        court_case.save()
        
        still_open = False
        suspects = case.legalcasesuspect_set.all()
        for suspect in suspects:
            sf = None
            find_name = suspect.person.full_name.lower().strip()
            infos = SuspectInformation.objects.filter(suspect__incidents=incident)
            for info in infos:
                if find_name == info.person.full_name.lower().strip():
                    sf = info.suspect
                    break
            if sf is None:
                print ('Suspect for case', case.legal_case_number, 'name', suspect.person.full_name)
                continue
            
            lc_suspect = LegalChargeSuspect()
            lc_suspect.legal_charge = legal_charge
            lc_suspect.sf = sf
            lc_suspect.arrest_status = suspect.arrest_status
            lc_suspect.named_on_charge_sheet = suspect.named_on_charge_sheet
            lc_suspect.arrest_date = suspect.arrest_date
            lc_suspect.arrest_submitted_date = suspect.arrest_submitted_date
            lc_suspect.court_cases = '1'
            lc_suspect.save()
            
            for theCharge in theCharges:
                charge = LegalChargeSuspectCharge()
                charge.legal_charge = legal_charge
                charge.sf = sf
                charge.court_case_sequence = '1'
                charge.charge = theCharge
                #charge.charge
                if suspect.verdict != 'Convicted' and suspect.verdict != 'Acquittal':
                    still_open = True
                charge.verdict = suspect.verdict
                charge.sentence_attached
                charge.verdict_date = suspect.verdict_date
                charge.verdict_submitted_date = suspect.verdict_submitted_date
                charge.imprisonment_years =suspect.imprisonment_years
                if suspect.imprisonment_total_days is not None:
                    charge.imprisonment_days = suspect.imprisonment_total_days % 365
                else:
                    charge.imprisonment_days = suspect.imprisonment_days
                charge.imprisonment_total_days = suspect.imprisonment_total_days
                charge.fine_amount = suspect.fine_amount
                charge.fine_currency = suspect.fine_currency
                charge.save()
        
        if still_open:
            court_case.status = 'Awaiting Verdict'
        else:
            court_case.status = 'Verdict Rendered'
        court_case.save()
    
        victims = case.legalcasevictim_set.all()
        for victim in victims:
            find_name = victim.person.full_name.lower().strip()
            pvf = None
            vdfs = VdfCommon.objects.filter(vdf_number__startswith=base_number)
            for vdf in vdfs:
                vdf_base = vdf.vdf_number
                for idx in range(len(vdf.station.station_code), len(vdf.vdf_number)):
                    the_char = vdf.vdf_number[idx]
                    if (the_char < '0' or the_char > '9') and the_char != '_':
                        vdf_base = vdf.vdf_number[:idx]
                        break
                if vdf_base != base_number:
                    continue
                if vdf.victim.full_name.lower().strip() == find_name:
                    pvf = vdf
                    break
            if pvf is None:
                print ('Victim for case', case.legal_case_number, 'name', vdf.victim.full_name)
                continue
        
            lc_victim = LegalChargeVictim()
            lc_victim.legal_charge = legal_charge
            lc_victim.pvf = pvf
            lc_victim.alternate_phone = victim.alternate_phone
            lc_victim.last_contact_date = victim.last_contact_date
            lc_victim.last_attempted_contact_date = victim.last_attempted_contact_date
            lc_victim.victim_status = victim.victim_status
            lc_victim.court_cases = '1'
            lc_victim.save()
            
        timeline_entries = case.legalcasetimeline_set.all()
        for entry in timeline_entries:
            lc_timeline = LegalChargeTimeline()  
            lc_timeline.legal_charge = legal_charge
            lc_timeline.comment_date = entry.comment_date
            lc_timeline.comment = entry.comment
            lc_timeline.added_by = entry.added_by
            lc_timeline.date_added = entry.date_added
            lc_timeline.date_removed = entry.date_removed
            lc_timeline.save()
            
        attachments = case.legalcaseattachment_set.all().order_by('id')
        attachment_number = 1
        for attachment in attachments:
            lc_attach = LegalChargeAttachment()
            lc_attach.legal_charge = legal_charge
            lc_attach.attachment_number = attachment_number
            lc_attach.description = attachment.description
            lc_attach.attachment = attachment.attachment
            lc_attach.private_card = attachment.private_card
            lc_attach.option = attachment.option
            lc_attach.save()
            
            attachment_number += 1

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0258_auto_20230824_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourtCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.PositiveIntegerField()),
                ('court_case', models.CharField(max_length=127, null=True)),
                ('status', models.CharField(max_length=127, null=True)),
                ('charges', models.CharField(max_length=255, null=True)),
                ('specific_code_law', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20, verbose_name='Status')),
                ('date_time_entered_into_system', models.DateTimeField(auto_now_add=True)),
                ('date_time_last_updated', models.DateTimeField(auto_now=True)),
                ('form_version', models.CharField(max_length=126, null=True)),
                ('legal_charge_number', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=127, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('charge_sheet_date', models.DateField(null=True)),
                ('police_case', models.CharField(max_length=127, null=True)),
                ('human_trafficking', models.CharField(max_length=255, null=True)),
                ('case_summary', models.TextField(null=True)),
                ('date_last_contacted', models.DateField(null=True)),
                ('missing_data_count', models.PositiveIntegerField(blank=True, null=True)),
                ('form_entered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='legalcharge_entered_by', to=settings.AUTH_USER_MODEL)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Incident')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.BorderStation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=126, null=True)),
                ('attachment', models.FileField(upload_to='legal_case_attachments', verbose_name='Attach scanned copy of form (pdf or image)')),
                ('private_card', models.BooleanField(default=True)),
                ('option', models.CharField(max_length=126, null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeSuspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrest_status', models.CharField(max_length=255, null=True)),
                ('named_on_charge_sheet', models.CharField(max_length=127, null=True)),
                ('arrest_date', models.DateField(null=True)),
                ('arrest_submitted_date', models.DateField(null=True)),
                ('court_cases', models.CharField(max_length=255, null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
                ('sf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeSuspectCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_case_sequence', models.PositiveIntegerField()),
                ('charge', models.CharField(max_length=127, null=True)),
                ('verdict', models.CharField(max_length=127, null=True)),
                ('sentence_attached', models.CharField(max_length=127, null=True)),
                ('verdict_date', models.DateField(null=True)),
                ('verdict_submitted_date', models.DateField(null=True)),
                ('imprisonment_years', models.PositiveIntegerField(blank=True, null=True)),
                ('imprisonment_days', models.PositiveIntegerField(blank=True, null=True)),
                ('imprisonment_total_days', models.PositiveIntegerField(blank=True, null=True)),
                ('fine_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('fine_currency', models.CharField(max_length=255, null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
                ('sf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateField()),
                ('comment', models.TextField()),
                ('added_by', models.CharField(max_length=255, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_removed', models.DateField(null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_case_sequence', models.PositiveIntegerField()),
                ('verified_attachment', models.CharField(max_length=127, null=True)),
                ('taken_into_custody', models.CharField(max_length=127, null=True)),
                ('charged_with_crime', models.CharField(max_length=127, null=True)),
                ('police_case_or_court_case', models.CharField(max_length=127, null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
                ('sf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Suspect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegalChargeVictim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternate_phone', models.CharField(max_length=255, null=True)),
                ('last_contact_date', models.DateField(null=True)),
                ('last_attempted_contact_date', models.DateField(null=True)),
                ('victim_status', models.CharField(max_length=255, null=True)),
                ('court_cases', models.CharField(max_length=255, null=True)),
                ('legal_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge')),
                ('pvf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.VdfCommon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='courtcase',
            name='legal_charge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legal.LegalCharge'),
        ),
        migrations.CreateModel(
            name='LegalChargeCountrySpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge', models.CharField(max_length=127, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataentry.Country')),
            ],
        ),
        migrations.RunSQL("insert into legal_legalchargecountryspecific (country_id, charge) values (1, 'Human Trafficking and Transportation (Control) Act (2064)')"),
        migrations.RunSQL("insert into legal_legalchargecountryspecific (country_id, charge) values (1, 'Civil Criminal Procedure Code 2074')"),
        migrations.RunSQL("insert into legal_legalchargecountryspecific (country_id, charge) values (1, 'Domestic Violence and Punishment Act 2066')"),
        migrations.RunSQL("insert into legal_legalchargecountryspecific (country_id, charge) values (1, 'Foreign Employment Act 2064')"),
        
        migrations.RunPython(migrate_legal_charge)
    ]
