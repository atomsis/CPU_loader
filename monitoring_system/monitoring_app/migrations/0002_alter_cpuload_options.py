# Generated by Django 5.0.4 on 2024-05-01 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpuload',
            options={'get_latest_by': 'timestamp'},
        ),
    ]
