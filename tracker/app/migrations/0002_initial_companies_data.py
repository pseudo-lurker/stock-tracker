# Generated by Django 5.0.2 on 2024-03-01 06:52

from django.db import migrations


def populate_initial_companies(apps, schema_editor):
    company_model = apps.get_model('app', 'Company')
    company_model.objects.create(
        ticker='GOOGL',
        name='Google'
    )

    company_model.objects.create(
        ticker='AMZN',
        name='Amazon'
    )

    company_model.objects.create(
        ticker='MSFT',
        name='Microsoft'
    )


class Migration(migrations.Migration):
    dependencies = [('app', '0001_initial')]

    operations = [migrations.RunPython(populate_initial_companies)]
