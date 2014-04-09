# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Interceptee'
        db.create_table(u'dataentry_interceptee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interception_record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interceptees', to=orm['dataentry.InterceptionRecord'])),
            ('kind', self.gf('django.db.models.fields.IntegerField')()),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('vdc', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('phone_contact', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('relation_to', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'dataentry', ['Interceptee'])

        # Adding field 'InterceptionRecord.contact_noticed'
        db.add_column(u'dataentry_interceptionrecord', 'contact_noticed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_hotel_owner'
        db.add_column(u'dataentry_interceptionrecord', 'contact_hotel_owner',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_rickshaw_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_rickshaw_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_taxi_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_taxi_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_bus_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_bus_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_church_member'
        db.add_column(u'dataentry_interceptionrecord', 'contact_church_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other_ngo'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other_ngo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_police'
        db.add_column(u'dataentry_interceptionrecord', 'contact_police',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_subcommittee_member'
        db.add_column(u'dataentry_interceptionrecord', 'contact_subcommittee_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other_value'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_paid_no'
        db.add_column(u'dataentry_interceptionrecord', 'contact_paid_no',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_paid_yes'
        db.add_column(u'dataentry_interceptionrecord', 'contact_paid_yes',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_paid_how_much'
        db.add_column(u'dataentry_interceptionrecord', 'contact_paid_how_much',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.staff_noticed'
        db.add_column(u'dataentry_interceptionrecord', 'staff_noticed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.staff_who_noticed'
        db.add_column(u'dataentry_interceptionrecord', 'staff_who_noticed',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_hesitant'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_hesitant',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_nervous_or_afraid'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_nervous_or_afraid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_hurrying'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_hurrying',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_drugged_or_drowsy'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_drugged_or_drowsy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_new_clothes'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_new_clothes',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_dirty_clothes'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_dirty_clothes',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_carrying_full_bags'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_carrying_full_bags',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_village_dress'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_village_dress',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_indian_looking'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_indian_looking',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_typical_village_look'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_typical_village_look',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_looked_like_agent'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_looked_like_agent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_caste_difference'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_caste_difference',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_young_looking'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_young_looking',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_waiting_sitting'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_waiting_sitting',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_walking_to_border'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_walking_to_border',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_roaming_around'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_roaming_around',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_exiting_vehicle'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_exiting_vehicle',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_heading_to_vehicle'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_heading_to_vehicle',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_in_a_vehicle'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_in_a_vehicle',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_in_a_rickshaw'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_in_a_rickshaw',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_in_a_cart'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_in_a_cart',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_carrying_a_baby'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_carrying_a_baby',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.noticed_on_the_phone'
        db.add_column(u'dataentry_interceptionrecord', 'noticed_on_the_phone',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Interceptee'
        db.delete_table(u'dataentry_interceptee')

        # Deleting field 'InterceptionRecord.contact_noticed'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_noticed')

        # Deleting field 'InterceptionRecord.contact_hotel_owner'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_hotel_owner')

        # Deleting field 'InterceptionRecord.contact_rickshaw_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_rickshaw_driver')

        # Deleting field 'InterceptionRecord.contact_taxi_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_taxi_driver')

        # Deleting field 'InterceptionRecord.contact_bus_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_bus_driver')

        # Deleting field 'InterceptionRecord.contact_church_member'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_church_member')

        # Deleting field 'InterceptionRecord.contact_other_ngo'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other_ngo')

        # Deleting field 'InterceptionRecord.contact_police'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_police')

        # Deleting field 'InterceptionRecord.contact_subcommittee_member'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_subcommittee_member')

        # Deleting field 'InterceptionRecord.contact_other'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other')

        # Deleting field 'InterceptionRecord.contact_other_value'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other_value')

        # Deleting field 'InterceptionRecord.contact_paid_no'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_paid_no')

        # Deleting field 'InterceptionRecord.contact_paid_yes'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_paid_yes')

        # Deleting field 'InterceptionRecord.contact_paid_how_much'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_paid_how_much')

        # Deleting field 'InterceptionRecord.staff_noticed'
        db.delete_column(u'dataentry_interceptionrecord', 'staff_noticed')

        # Deleting field 'InterceptionRecord.staff_who_noticed'
        db.delete_column(u'dataentry_interceptionrecord', 'staff_who_noticed')

        # Deleting field 'InterceptionRecord.noticed_hesitant'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_hesitant')

        # Deleting field 'InterceptionRecord.noticed_nervous_or_afraid'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_nervous_or_afraid')

        # Deleting field 'InterceptionRecord.noticed_hurrying'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_hurrying')

        # Deleting field 'InterceptionRecord.noticed_drugged_or_drowsy'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_drugged_or_drowsy')

        # Deleting field 'InterceptionRecord.noticed_new_clothes'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_new_clothes')

        # Deleting field 'InterceptionRecord.noticed_dirty_clothes'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_dirty_clothes')

        # Deleting field 'InterceptionRecord.noticed_carrying_full_bags'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_carrying_full_bags')

        # Deleting field 'InterceptionRecord.noticed_village_dress'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_village_dress')

        # Deleting field 'InterceptionRecord.noticed_indian_looking'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_indian_looking')

        # Deleting field 'InterceptionRecord.noticed_typical_village_look'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_typical_village_look')

        # Deleting field 'InterceptionRecord.noticed_looked_like_agent'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_looked_like_agent')

        # Deleting field 'InterceptionRecord.noticed_caste_difference'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_caste_difference')

        # Deleting field 'InterceptionRecord.noticed_young_looking'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_young_looking')

        # Deleting field 'InterceptionRecord.noticed_waiting_sitting'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_waiting_sitting')

        # Deleting field 'InterceptionRecord.noticed_walking_to_border'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_walking_to_border')

        # Deleting field 'InterceptionRecord.noticed_roaming_around'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_roaming_around')

        # Deleting field 'InterceptionRecord.noticed_exiting_vehicle'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_exiting_vehicle')

        # Deleting field 'InterceptionRecord.noticed_heading_to_vehicle'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_heading_to_vehicle')

        # Deleting field 'InterceptionRecord.noticed_in_a_vehicle'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_in_a_vehicle')

        # Deleting field 'InterceptionRecord.noticed_in_a_rickshaw'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_in_a_rickshaw')

        # Deleting field 'InterceptionRecord.noticed_in_a_cart'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_in_a_cart')

        # Deleting field 'InterceptionRecord.noticed_carrying_a_baby'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_carrying_a_baby')

        # Deleting field 'InterceptionRecord.noticed_on_the_phone'
        db.delete_column(u'dataentry_interceptionrecord', 'noticed_on_the_phone')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dataentry.account': {
            'Meta': {'object_name': 'Account'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'dataentry.interceptee': {
            'Meta': {'object_name': 'Interceptee'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interception_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interceptees'", 'to': u"orm['dataentry.InterceptionRecord']"}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'phone_contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'relation_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'dataentry.interceptionrecord': {
            'Meta': {'object_name': 'InterceptionRecord'},
            'between_2_12_weeks_before_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'caste_not_same_as_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'caught_in_lie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_bus_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_church_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_hotel_owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_noticed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_other_ngo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_paid_how_much': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_paid_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_paid_yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_police': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_rickshaw_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_subcommittee_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_taxi_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'couldnt_confirm_job': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doesnt_know_going_to_india': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doesnt_know_school_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doesnt_know_villiage_details': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drugged_or_drowsy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fake_medical_documents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'going_to_gulf_for_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irf_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'less_than_2_weeks_before_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'married_in_past_2_8_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'married_in_past_2_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_someone_across_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_address_in_india': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_appointment_letter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_bags_long_trip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_company_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_enrollment_docs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_medical_appointment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_medical_documents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_school_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'not_enrolled_in_school': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'not_real_job': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_carrying_a_baby': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_carrying_full_bags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_caste_difference': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_dirty_clothes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_drugged_or_drowsy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_exiting_vehicle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_heading_to_vehicle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_hesitant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_hurrying': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_in_a_cart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_in_a_rickshaw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_in_a_vehicle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_indian_looking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_looked_like_agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_nervous_or_afraid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_new_clothes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_on_the_phone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_roaming_around': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_typical_village_look': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_village_dress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_waiting_sitting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_walking_to_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_young_looking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number_of_traffickers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_victims': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'over_18_family_doesnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'over_18_family_unwilling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_with_broker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'refuses_family_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_family_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_treatment_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_villiage_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reported_total_red_flags': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'running_away_over_18': ('django.db.models.fields.BooleanField', [], {}),
            'running_away_under_18': ('django.db.models.fields.BooleanField', [], {}),
            'seen_in_last_month_in_nepal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shopping_overnight_stuff_in_bags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'staff_noticed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff_who_noticed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'talked_to_aunt_uncle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_brother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_father': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_grandparent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_mother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'talked_to_sister': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'traveling_with_someone_not_with_her': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_cant_contact_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_family_doesnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_family_unwilling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid_gulf_country_visa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'who_in_group': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'wife_under_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['dataentry']