# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'InterceptionRecord.type_gulf_countries'
        db.delete_column(u'dataentry_interceptionrecord', 'type_gulf_countries')

        # Deleting field 'InterceptionRecord.type_circus'
        db.delete_column(u'dataentry_interceptionrecord', 'type_circus')

        # Deleting field 'InterceptionRecord.type_unsafe_migration'
        db.delete_column(u'dataentry_interceptionrecord', 'type_unsafe_migration')

        # Deleting field 'InterceptionRecord.type_india_trafficking'
        db.delete_column(u'dataentry_interceptionrecord', 'type_india_trafficking')

        # Deleting field 'InterceptionRecord.type_runaway'
        db.delete_column(u'dataentry_interceptionrecord', 'type_runaway')

        # Adding field 'InterceptionRecord.interception_type'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'InterceptionRecord.type_gulf_countries'
        db.add_column(u'dataentry_interceptionrecord', 'type_gulf_countries',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.type_circus'
        db.add_column(u'dataentry_interceptionrecord', 'type_circus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.type_unsafe_migration'
        db.add_column(u'dataentry_interceptionrecord', 'type_unsafe_migration',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.type_india_trafficking'
        db.add_column(u'dataentry_interceptionrecord', 'type_india_trafficking',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.type_runaway'
        db.add_column(u'dataentry_interceptionrecord', 'type_runaway',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'InterceptionRecord.interception_type'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type')


    models = {
        u'dataentry.interceptee': {
            'Meta': {'object_name': 'Interceptee'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interception_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interceptees'", 'to': u"orm['dataentry.InterceptionRecord']"}),
            'kind': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone_contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'relation_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'dataentry.interceptionrecord': {
            'Meta': {'object_name': 'InterceptionRecord'},
            'between_2_12_weeks_before_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'call_subcommittee_chair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'call_thn_to_cross_check': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'has_signature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'how_sure_was_trafficking': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interception_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'irf_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'job_too_good_to_be_true': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'less_than_2_weeks_before_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'married_in_past_2_8_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'married_in_past_2_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_someone_across_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_come_up_before_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_come_up_before_yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_come_up_before_yes_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
            'noticed_other_sign': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_other_sign_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'noticed_roaming_around': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_typical_village_look': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_village_dress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_waiting_sitting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_walking_to_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'noticed_young_looking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number_of_traffickers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_victims': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'other_red_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_red_flag_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'over_18_family_doesnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'over_18_family_unwilling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_with_broker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'refuses_family_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_family_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_treatment_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reluctant_villiage_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reported_total_red_flags': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'running_away_over_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'running_away_under_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scan_and_submit_same_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scanned_form': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
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
            'trafficker_taken_into_custody': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'traveling_with_someone_not_with_her': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_cant_contact_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_family_doesnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'under_18_family_unwilling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid_gulf_country_visa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going_job': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going_shopping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going_study': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going_treatment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'where_going_visit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_alone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_husbandwife': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wife_under_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['dataentry']