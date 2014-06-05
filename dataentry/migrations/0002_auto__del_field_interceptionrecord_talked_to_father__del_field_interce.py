# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'InterceptionRecord.talked_to_father'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_father')

        # Deleting field 'InterceptionRecord.contact_other_ngo'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other_ngo')

        # Deleting field 'InterceptionRecord.interception_type'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type')

        # Deleting field 'InterceptionRecord.contact_church_member'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_church_member')

        # Deleting field 'InterceptionRecord.talked_to_mother'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_mother')

        # Deleting field 'InterceptionRecord.contact_police'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_police')

        # Deleting field 'InterceptionRecord.contact_subcommittee_member'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_subcommittee_member')

        # Deleting field 'InterceptionRecord.talked_to_other'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_other')

        # Deleting field 'InterceptionRecord.name_come_up_before_yes_value'
        db.delete_column(u'dataentry_interceptionrecord', 'name_come_up_before_yes_value')

        # Deleting field 'InterceptionRecord.contact_other'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other')

        # Deleting field 'InterceptionRecord.talked_to_sister'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_sister')

        # Deleting field 'InterceptionRecord.contact_rickshaw_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_rickshaw_driver')

        # Deleting field 'InterceptionRecord.talked_to_grandparent'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_grandparent')

        # Deleting field 'InterceptionRecord.name_come_up_before'
        db.delete_column(u'dataentry_interceptionrecord', 'name_come_up_before')

        # Deleting field 'InterceptionRecord.contact_hotel_owner'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_hotel_owner')

        # Deleting field 'InterceptionRecord.contact_bus_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_bus_driver')

        # Deleting field 'InterceptionRecord.talked_to_brother'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_brother')

        # Deleting field 'InterceptionRecord.contact_other_value'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_other_value')

        # Deleting field 'InterceptionRecord.talked_to_other_value'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_other_value')

        # Deleting field 'InterceptionRecord.contact_taxi_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'contact_taxi_driver')

        # Deleting field 'InterceptionRecord.talked_to_aunt_uncle'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_aunt_uncle')

        # Adding field 'InterceptionRecord.talked_to_family_member_brother'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_brother',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_sister'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_sister',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_father'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_father',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_mother'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_mother',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_grandparent'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_grandparent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_aunt_uncle'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_aunt_uncle',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_other'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_family_member_other_value'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_family_member_other_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_hotel_owner'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_hotel_owner',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_rickshaw_driver'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_rickshaw_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_taxi_driver'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_taxi_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_bus_driver'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_bus_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_church_member'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_church_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_other_ngo'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_other_ngo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_police'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_police',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_subcommittee_member'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_subcommittee_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_other'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.which_contact_other_value'
        db.add_column(u'dataentry_interceptionrecord', 'which_contact_other_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.name_came_up_before'
        db.add_column(u'dataentry_interceptionrecord', 'name_came_up_before',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.name_came_up_before_value'
        db.add_column(u'dataentry_interceptionrecord', 'name_came_up_before_value',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type_gulf_countries'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type_gulf_countries',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type_india_trafficking'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type_india_trafficking',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type_unsafe_migration'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type_unsafe_migration',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type_circus'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type_circus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type_runaway'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type_runaway',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'InterceptionRecord.number_of_traffickers'
        db.alter_column(u'dataentry_interceptionrecord', 'number_of_traffickers', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'InterceptionRecord.trafficker_taken_into_custody'
        db.alter_column(u'dataentry_interceptionrecord', 'trafficker_taken_into_custody', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'InterceptionRecord.number_of_victims'
        db.alter_column(u'dataentry_interceptionrecord', 'number_of_victims', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))
        # Deleting field 'VictimInterview.date_time'
        db.delete_column(u'dataentry_victiminterview', 'date_time')

        # Adding field 'VictimInterview.date'
        db.add_column(u'dataentry_victiminterview', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'VictimInterview.number_of_traffickers'
        db.alter_column(u'dataentry_victiminterview', 'number_of_traffickers', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'VictimInterview.number_of_victims'
        db.alter_column(u'dataentry_victiminterview', 'number_of_victims', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):
        # Adding field 'InterceptionRecord.talked_to_father'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_father',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other_ngo'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other_ngo',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.interception_type'
        db.add_column(u'dataentry_interceptionrecord', 'interception_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_church_member'
        db.add_column(u'dataentry_interceptionrecord', 'contact_church_member',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_mother'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_mother',
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

        # Adding field 'InterceptionRecord.talked_to_other'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.name_come_up_before_yes_value'
        db.add_column(u'dataentry_interceptionrecord', 'name_come_up_before_yes_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_sister'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_sister',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_rickshaw_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_rickshaw_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_grandparent'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_grandparent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.name_come_up_before'
        db.add_column(u'dataentry_interceptionrecord', 'name_come_up_before',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_hotel_owner'
        db.add_column(u'dataentry_interceptionrecord', 'contact_hotel_owner',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_bus_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_bus_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_brother'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_brother',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_other_value'
        db.add_column(u'dataentry_interceptionrecord', 'contact_other_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_other_value'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_other_value',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'InterceptionRecord.contact_taxi_driver'
        db.add_column(u'dataentry_interceptionrecord', 'contact_taxi_driver',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'InterceptionRecord.talked_to_aunt_uncle'
        db.add_column(u'dataentry_interceptionrecord', 'talked_to_aunt_uncle',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'InterceptionRecord.talked_to_family_member_brother'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_brother')

        # Deleting field 'InterceptionRecord.talked_to_family_member_sister'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_sister')

        # Deleting field 'InterceptionRecord.talked_to_family_member_father'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_father')

        # Deleting field 'InterceptionRecord.talked_to_family_member_mother'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_mother')

        # Deleting field 'InterceptionRecord.talked_to_family_member_grandparent'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_grandparent')

        # Deleting field 'InterceptionRecord.talked_to_family_member_aunt_uncle'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_aunt_uncle')

        # Deleting field 'InterceptionRecord.talked_to_family_member_other'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_other')

        # Deleting field 'InterceptionRecord.talked_to_family_member_other_value'
        db.delete_column(u'dataentry_interceptionrecord', 'talked_to_family_member_other_value')

        # Deleting field 'InterceptionRecord.which_contact_hotel_owner'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_hotel_owner')

        # Deleting field 'InterceptionRecord.which_contact_rickshaw_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_rickshaw_driver')

        # Deleting field 'InterceptionRecord.which_contact_taxi_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_taxi_driver')

        # Deleting field 'InterceptionRecord.which_contact_bus_driver'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_bus_driver')

        # Deleting field 'InterceptionRecord.which_contact_church_member'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_church_member')

        # Deleting field 'InterceptionRecord.which_contact_other_ngo'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_other_ngo')

        # Deleting field 'InterceptionRecord.which_contact_police'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_police')

        # Deleting field 'InterceptionRecord.which_contact_subcommittee_member'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_subcommittee_member')

        # Deleting field 'InterceptionRecord.which_contact_other'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_other')

        # Deleting field 'InterceptionRecord.which_contact_other_value'
        db.delete_column(u'dataentry_interceptionrecord', 'which_contact_other_value')

        # Deleting field 'InterceptionRecord.name_came_up_before'
        db.delete_column(u'dataentry_interceptionrecord', 'name_came_up_before')

        # Deleting field 'InterceptionRecord.name_came_up_before_value'
        db.delete_column(u'dataentry_interceptionrecord', 'name_came_up_before_value')

        # Deleting field 'InterceptionRecord.interception_type_gulf_countries'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type_gulf_countries')

        # Deleting field 'InterceptionRecord.interception_type_india_trafficking'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type_india_trafficking')

        # Deleting field 'InterceptionRecord.interception_type_unsafe_migration'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type_unsafe_migration')

        # Deleting field 'InterceptionRecord.interception_type_circus'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type_circus')

        # Deleting field 'InterceptionRecord.interception_type_runaway'
        db.delete_column(u'dataentry_interceptionrecord', 'interception_type_runaway')


        # Changing field 'InterceptionRecord.number_of_traffickers'
        db.alter_column(u'dataentry_interceptionrecord', 'number_of_traffickers', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'InterceptionRecord.trafficker_taken_into_custody'
        db.alter_column(u'dataentry_interceptionrecord', 'trafficker_taken_into_custody', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'InterceptionRecord.number_of_victims'
        db.alter_column(u'dataentry_interceptionrecord', 'number_of_victims', self.gf('django.db.models.fields.IntegerField')(null=True))

        # User chose to not deal with backwards NULL issues for 'VictimInterview.date_time'
        raise RuntimeError("Cannot reverse this migration. 'VictimInterview.date_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'VictimInterview.date_time'
        db.add_column(u'dataentry_victiminterview', 'date_time',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'VictimInterview.date'
        db.delete_column(u'dataentry_victiminterview', 'date')


        # Changing field 'VictimInterview.number_of_traffickers'
        db.alter_column(u'dataentry_victiminterview', 'number_of_traffickers', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'VictimInterview.number_of_victims'
        db.alter_column(u'dataentry_victiminterview', 'number_of_victims', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'activation_key': ('django.db.models.fields.CharField', [], {'default': "'y9TW9pW9EPnqbC21ncMbnMEJ3bzW9a5MsRPm0040'", 'max_length': '40'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'permission_accounts_manage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_designation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts'", 'to': u"orm['accounts.DefaultPermissionsSet']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'accounts.defaultpermissionsset': {
            'Meta': {'object_name': 'DefaultPermissionsSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'permission_accounts_manage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_irf_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_vif_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
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
        u'dataentry.interceptee': {
            'Meta': {'ordering': "['id']", 'object_name': 'Interceptee'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interception_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interceptees'", 'to': u"orm['dataentry.InterceptionRecord']"}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
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
            'contact_noticed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_paid': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'contact_paid_how_much': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'couldnt_confirm_job': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_form_received': ('django.db.models.fields.DateTimeField', [], {}),
            'date_time_entered_into_system': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_time_last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_time_of_interception': ('django.db.models.fields.DateTimeField', [], {}),
            'doesnt_know_going_to_india': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doesnt_know_school_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'doesnt_know_villiage_details': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drugged_or_drowsy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fake_medical_documents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'form_entered_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'irfs_entered'", 'to': u"orm['accounts.Account']"}),
            'going_to_gulf_for_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_signature': ('django.db.models.fields.BooleanField', [], {}),
            'how_sure_was_trafficking': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interception_type_circus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interception_type_gulf_countries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interception_type_india_trafficking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interception_type_runaway': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interception_type_unsafe_migration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'irf_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'job_too_good_to_be_true': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'less_than_2_weeks_before_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'married_in_past_2_8_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'married_in_past_2_weeks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_someone_across_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_came_up_before': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name_came_up_before_value': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'number_of_traffickers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_victims': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'staff_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'staff_noticed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'staff_who_noticed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'talked_to_family_member_aunt_uncle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_brother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_father': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_grandparent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_mother': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'talked_to_family_member_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'talked_to_family_member_sister': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trafficker_taken_into_custody': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'which_contact_bus_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_church_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_hotel_owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_other_ngo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'which_contact_police': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_rickshaw_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_subcommittee_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_contact_taxi_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_alone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_husbandwife': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'who_in_group_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wife_under_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dataentry.victiminterview': {
            'Meta': {'object_name': 'VictimInterview'},
            'abuse_happened_by_whom': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'abuse_happened_denied_proper_food': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'abuse_happened_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'abuse_happened_forced_to_take_drugs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'abuse_happened_physical_abuse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'abuse_happened_sexual_abuse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'abuse_happened_sexual_harassment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'abuse_happened_threats': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'amount_victim_would_earn': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'attitude_towards_tiny_hands_blames': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attitude_towards_tiny_hands_doesnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attitude_towards_tiny_hands_thankful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'awareness_before_interception_had_heard_not_how_bad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'awareness_before_interception_knew_how_bad_not_happening_to_her': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'awareness_before_interception_never_heard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'broker_works_in_job_location_dont_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'broker_works_in_job_location_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'broker_works_in_job_location_yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_boyfriend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_contractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_friend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_husband': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_neighbor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'brokers_relation_to_victim_own_aunt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_bro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_dad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_mom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_other_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_sister': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_own_uncle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'brokers_relation_to_victim_recently_met': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'case_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'companion_with_when_intercepted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'date_time_entered_into_system': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_time_last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'family_pressured_victim': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'family_will_try_sending_again': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'guardian_knew_was_travelling_to_india': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_signature': ('django.db.models.fields.BooleanField', [], {}),
            'how_can_we_serve_you_better': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'how_many_others_in_situation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'interviewer_recommendation_find_other_place': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewer_recommendation_send_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewer_recommendation_send_to_other_relatives': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legal_action_against_traffickers_dofe_complaint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legal_action_against_traffickers_fir_filed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legal_action_against_traffickers_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legal_action_dofe_against_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'legal_action_fir_against_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'manpower_involved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'meeting_at_border_meeting_broker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_at_border_meeting_companion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_at_border_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_at_border_yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_arranged_marriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_education': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_eloping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_baby_care': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_broker_didnt_say': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_brothel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_factory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_hotel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_household': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_laborer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_job_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'migration_plans_job_shop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_medical_treatment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_meet_own_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'migration_plans_shopping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_travel_tour': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'migration_plans_visit_brokers_home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'money_changed_hands_broker_companion_broker_gave_money': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'money_changed_hands_broker_companion_companion_gave_money': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'money_changed_hands_broker_companion_dont_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'money_changed_hands_broker_companion_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number_broker_made_similar_promises_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_traffickers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_victims': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'other_involved_husband_trafficker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'other_involved_person_in_india': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'other_involved_place_involved_in_trafficking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'other_involved_someone_involved_in_trafficking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'other_involved_someone_met_along_the_way': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'other_people_and_places_involved': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'others_in_situation_age_of_youngest': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passport_made_no_passport_made': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_made_passport_included_false_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_made_passport_included_other_false_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_made_passport_was_fake': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'passport_made_real_passport_made': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'permission_to_use_photograph': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'planning_to_meet_companion_later': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'primary_motivation_bad_home_marriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_didnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_family_debt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_get_education': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_love_marriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'primary_motivation_personal_debt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_support_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_support_myself': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_motivation_tour_travel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_family_afraid_for_safety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_family_afraid_of_reputation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_interference_by_powerful_people': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_interference_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'reason_no_legal_no_trafficking_suspected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'reason_no_legal_police_bribed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_police_not_enough_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_she_was_going_herself': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_trafficker_is_own_people': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_trafficker_ran_away': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_victim_afraid_for_safety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_victim_afraid_of_reputation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason_no_legal_victim_family_bribed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reported_total_situational_alarms': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scanned_form': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'statement_read_before_beginning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tiny_hands_rating_border_staff': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tiny_hands_rating_shelter_accommodations': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tiny_hands_rating_shelter_staff': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tiny_hands_rating_trafficking_awareness': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'victim_address_district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_address_vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_address_ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_age': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_beliefs_now_believes_and_church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_beliefs_now_believes_no_church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_beliefs_now_doesnt_believe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_brahmin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_chhetri': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_dalit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_jaisi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_madeshi_terai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_magar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_mongolian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_muslim': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_newar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_caste_tamang': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_caste_thakuri': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_11_12': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_bachelors': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_grade_4_8': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_grade_9_10': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_informal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_masters': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_none': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_education_level_slc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_family_economic_situation_comfortable_basic_needs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_family_economic_situation_difficult_basic_needs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_family_economic_situation_no_basic_needs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_family_economic_situation_wealthy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_feels_safe_at_home': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_first_time_crossing_border': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_gender': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'victim_guardian_address_district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_guardian_address_vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_guardian_address_ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_guardian_drinks_alcohol_all_the_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_guardian_drinks_alcohol_never': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_guardian_drinks_alcohol_occasionally': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_guardian_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_guardian_uses_drugs_all_the_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_guardian_uses_drugs_never': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_guardian_uses_drugs_occasionally': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_had_suicidal_thoughts': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_has_worked_in_sex_industry': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_heard_gospel_already_believer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_heard_gospel_heard_but_never_believed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_heard_gospel_heard_name_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_heard_gospel_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_home_had_emotional_abuse_frequently': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_emotional_abuse_never': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_emotional_abuse_rarely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_physical_abuse_frequently': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_physical_abuse_never': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_physical_abuse_rarely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_sexual_abuse_frequently': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_sexual_abuse_never': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_home_had_sexual_abuse_rarely': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_expense_was_paid_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'victim_how_expense_was_paid_broker_gave_loan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_expense_was_paid_broker_paid_all': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_expense_was_paid_gave_money_to_broker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_expense_was_paid_paid_myself': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_long_known_broker_months': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_how_long_known_broker_years': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_how_long_stayed_between_days': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_how_long_stayed_between_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'victim_how_met_broker_at_school': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_at_wedding': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_at_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_called_my_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_from_community': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_he_approached_me': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_in_a_hospital': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_in_a_vehicle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_job_advertisement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_mobile_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'victim_how_met_broker_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_how_met_broker_through_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_through_friends': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_how_met_broker_went_myself': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_is_literate': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_knew_details_about_destination': ('django.db.models.fields.BooleanField', [], {}),
            'victim_lives_with_alone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_friends': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_husband': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_husbands_family': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_other_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_lives_with_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_lives_with_own_parents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_abandoned_by_husband': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_divorced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_husband_has_other_wives': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_married': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_single': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_marital_status_widow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_married_to_broker_months': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_married_to_broker_years': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'victim_num_in_family': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'victim_occupation_animal_husbandry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_business_owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_domestic_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_factory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_farmer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_hotel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_housewife': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_migrant_worker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_occupation_shopkeeper': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_tailoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_unemployed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_occupation_wage_laborer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_divorced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_separated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_status_father_has_other_wives': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_status_married': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_status_single': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_parents_marital_status_widow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_passport_with_broker': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_place_worked_involved_sending_girls_overseas': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_primary_guardian_husband': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_guardian_no_one': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_guardian_non_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_guardian_other_relative': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_guardian_own_parents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_local_bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_microbus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_motorbike': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_primary_means_of_travel_plane': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_private_car': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_primary_means_of_travel_tourist_bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_recruited_in_village': ('django.db.models.fields.BooleanField', [], {}),
            'victim_stayed_somewhere_between': ('django.db.models.fields.BooleanField', [], {}),
            'victim_traveled_with_broker_companion_broker_took_me_to_border': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_traveled_with_broker_companion_no': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_traveled_with_broker_companion_yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_wants_to_go_home': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_was_free_to_go_out': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_was_free_to_go_out_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'victim_was_hidden': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victim_was_hidden_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'victim_weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_where_going_bihar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_delhi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_dubai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_gulf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_gulf_didnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_gulf_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_gulf_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_where_going_india': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_india_didnt_know': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_india_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_india_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_where_going_jaipur': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_kolkata': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_kuwait': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_lebanon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_malaysia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_mumbai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_oman': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_pune': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_qatar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_rajastan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_saudi_arabia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_where_going_surat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vif_number': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'dataentry.victiminterviewlocationbox': {
            'Meta': {'object_name': 'VictimInterviewLocationBox'},
            'associated_with_person': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'associated_with_person_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'compound_wall': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gate_color': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewer_believes_not_used_for_trafficking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewer_believes_suspect_used_for_trafficking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewer_believes_trafficked_many_girls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewer_believes_trafficked_some_girls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location_in_town': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nearby_landmarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nearby_signboards': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'number_of_levels': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'person_in_charge': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'roof_color': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'roof_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'signboard': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_believes_not_used_for_trafficking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_believes_suspect_used_for_trafficking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_believes_trafficked_many_girls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_believes_trafficked_some_girls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'victim_interview': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_boxes'", 'to': u"orm['dataentry.VictimInterview']"}),
            'what_kind_place_brothel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_bus_station': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_factory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_hotel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_persons_house': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_shop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'what_kind_place_train_station': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_destination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_india_meetpoint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_known_location': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_manpower': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_nepal_meet_point': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_passport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_sex_industry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'which_place_transit_hideout': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dataentry.victiminterviewpersonbox': {
            'Meta': {'object_name': 'VictimInterviewPersonBox'},
            'address_district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_vdc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_ward': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'appearance_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'associated_with_place': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'associated_with_place_value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewer_believes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'occupation_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'physical_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'political_party': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'political_party_other_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_believes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'victim_interview': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_boxes'", 'to': u"orm['dataentry.VictimInterview']"}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'where_spends_time': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'who_is_this_relationship': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'who_is_this_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['dataentry']