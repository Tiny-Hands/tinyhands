# Generated by Django 4.2.10 on 2024-04-11 11:15

from django.db import migrations, models

def add_request(mdf, request_class, category, subcategory, cost, description):
    if cost > 0:
        request = request_class()
        request.project = mdf.border_station
        request.status = 'Approved-Completed'
        request.category = category
        request.original_cost = cost
        request.cost = cost
        request.description = description
        request.monthly = False
        request.benefit_type_name = subcategory
        request.completed_date_time = mdf.month_year
        request.save()
    
        mdf.requests.add(request)

def populate_food_and_stationary(apps, schema_editor):
    mod = __import__('budget.models', fromlist=['MonthlyDistributionForm','ProjectRequest'])
    mdf_class = getattr(mod, 'MonthlyDistributionForm', None)
    request_class = getattr(mod, 'ProjectRequest', None)
    
    mdfs = mdf_class.objects.filter(status='Approved')
    for mdf in mdfs:
        pv_food_total = mdf.food_and_snacks_intercepted_pv_total()
        add_request(mdf, request_class, 5, 'PV Food', pv_food_total, 'Total PV Food & Snacks Cost')
        
        limbo_food_total = mdf.limbo_total()
        add_request(mdf, request_class, 5, 'PV Food', limbo_food_total, 'Total Limbo PV Cost')
        
        stationary_total = mdf.stationery_total()
        add_request(mdf, request_class, 3, 'Stationary', stationary_total, 'Stationary Total')


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0016_mdfitem_approved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlydistributionform',
            name='money_not_spent_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monthlydistributionform',
            name='past_month_sent_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mdfitem',
            name='associated_section',
            field=models.IntegerField(blank=True, null=True, verbose_name=[(1, 'Staff Travel'), (3, 'Supplies & Awareness'), (5, 'Potential Victim Care'), (7, 'Communication'), (8, 'Salaries & Benefits'), (10, 'Administration'), (11, 'Past Month Sent Money'), (12, 'Limbo Potential Victims'), (13, 'Money Not Spent'), (14, 'Operational Expenses'), (15, 'Rent & Utilities'), (16, 'Multipliers'), (17, 'Guides')]),
        ),
        migrations.AlterField(
            model_name='monthlydistributionmultipliers',
            name='category',
            field=models.IntegerField(verbose_name=[(1, 'Staff Travel'), (3, 'Supplies & Awareness'), (5, 'Potential Victim Care'), (7, 'Communication'), (8, 'Salaries & Benefits'), (10, 'Administration'), (11, 'Past Month Sent Money'), (12, 'Limbo Potential Victims'), (13, 'Money Not Spent'), (14, 'Operational Expenses'), (15, 'Rent & Utilities'), (16, 'Multipliers'), (17, 'Guides')]),
        ),
        migrations.AlterField(
            model_name='projectrequest',
            name='category',
            field=models.IntegerField(verbose_name=[(8, 'Salaries & Benefits'), (15, 'Rent & Utilities'), (10, 'Administration'), (3, 'Supplies & Awareness'), (1, 'Staff Travel'), (5, 'Potential Victim Care'), (14, 'Operational Expenses'), (17, 'Guides')]),
        ),
        migrations.RunSQL("update budget_monthlydistributionform set past_month_sent_reviewed=true, money_not_spent_reviewed=true where status='Approved'"),
        migrations.RunSQL("update budget_projectrequest set benefit_type_name='Other' where category in (3,5)"),
        migrations.RunPython(populate_food_and_stationary),
    ]