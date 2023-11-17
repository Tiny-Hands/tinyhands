# Generated by Django 4.2.7 on 2023-11-17 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataentry', '0258_auto_20230509_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='params',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='audit',
            name='template',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='auditsample',
            name='results',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='cifcommon',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='condition',
            name='condition',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='options',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='verification_goals',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='exportimportfield',
            name='arguments_json',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='formcategory',
            name='form_category_question_config',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='formvalidation',
            name='params',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='gospelverification',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incident',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='indicatorhistory',
            name='indicators',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='interceptioncache',
            name='interceptions',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='interceptionrecord',
            name='contact_paid',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='interceptionrecord',
            name='name_came_up_before',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='irfcommon',
            name='contact_paid',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='irfcommon',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='legalcase',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='locationboxcommon',
            name='address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='locationform',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='locationform',
            name='merged_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='locationinformation',
            name='address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='matchhistory',
            name='match_results',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='monthlyreport',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='master_set_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='address_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.addresstype'),
        ),
        migrations.AlterField(
            model_name='persondocument',
            name='document_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.documenttype'),
        ),
        migrations.AlterField(
            model_name='personmatch',
            name='match_results',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='phone_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.phonetype'),
        ),
        migrations.AlterField(
            model_name='personsocialmedia',
            name='social_media_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.socialmediatype'),
        ),
        migrations.AlterField(
            model_name='question',
            name='export_params',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='params',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='questionlayout',
            name='form_config',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='data',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='storage',
            name='parent_storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataentry.storage'),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='suspectlegal',
            name='location_last_address',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='vdfcommon',
            name='form_entered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='companion_with_when_intercepted',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='family_pressured_victim',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='family_will_try_sending_again',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='guardian_knew_was_travelling_to_india',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='manpower_involved',
            field=models.BooleanField(null=True, verbose_name='Was a manpower involved?'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_involved_husband_trafficker',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_involved_person_in_india',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_involved_place_involved_in_trafficking',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_involved_someone_involved_in_trafficking',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_involved_someone_met_along_the_way',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='other_people_and_places_involved',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='planning_to_meet_companion_later',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_feels_safe_at_home',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_first_time_crossing_border',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_had_suicidal_thoughts',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_has_worked_in_sex_industry',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_is_literate',
            field=models.BooleanField(null=True, verbose_name='Is the victim literate?'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_passport_with_broker',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_place_worked_involved_sending_girls_overseas',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_wants_to_go_home',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_was_free_to_go_out',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_was_hidden',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_didnt_know',
            field=models.BooleanField(null=True, verbose_name='Did Not Know'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_dubai',
            field=models.BooleanField(null=True, verbose_name='Dubai'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_kuwait',
            field=models.BooleanField(null=True, verbose_name='Kuwait'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_lebanon',
            field=models.BooleanField(null=True, verbose_name='Lebanon'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_malaysia',
            field=models.BooleanField(null=True, verbose_name='Malaysia'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_oman',
            field=models.BooleanField(null=True, verbose_name='Oman'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_other',
            field=models.BooleanField(null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_qatar',
            field=models.BooleanField(null=True, verbose_name='Qatar'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_gulf_saudi_arabia',
            field=models.BooleanField(null=True, verbose_name='Saudi Arabia'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_bihar',
            field=models.BooleanField(null=True, verbose_name='Bihar'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_delhi',
            field=models.BooleanField(null=True, verbose_name='Delhi'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_didnt_know',
            field=models.BooleanField(null=True, verbose_name='Did Not Know'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_jaipur',
            field=models.BooleanField(null=True, verbose_name='Jaipur'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_kolkata',
            field=models.BooleanField(null=True, verbose_name='Kolkata'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_mumbai',
            field=models.BooleanField(null=True, verbose_name='Mumbai'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_other',
            field=models.BooleanField(null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_pune',
            field=models.BooleanField(null=True, verbose_name='Pune'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_rajastan',
            field=models.BooleanField(null=True, verbose_name='Rajastan'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_india_surat',
            field=models.BooleanField(null=True, verbose_name='Surat'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_region_gulf',
            field=models.BooleanField(null=True, verbose_name='Gulf / Other'),
        ),
        migrations.AlterField(
            model_name='victiminterview',
            name='victim_where_going_region_india',
            field=models.BooleanField(null=True, verbose_name='India'),
        ),
        migrations.AlterField(
            model_name='victiminterviewlocationbox',
            name='associated_with_person',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='victiminterviewpersonbox',
            name='associated_with_place',
            field=models.BooleanField(null=True),
        ),
    ]
