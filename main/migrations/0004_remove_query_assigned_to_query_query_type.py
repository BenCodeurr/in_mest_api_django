# Generated by Django 5.0.1 on 2024-03-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_classschedule_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='query',
            name='query_type',
            field=models.CharField(choices=[('FACILITY', 'Facility'), ('LOGISTICS', 'Logistics'), ('KITCHEN', 'Kitchen')], default='FACILITY', max_length=20),
        ),
    ]
