# Generated by Django 4.0.5 on 2022-06-18 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0004_policyterm_billing_system'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainsliderdata',
            name='price_badge_image',
        ),
    ]
