# Generated by Django 4.2.3 on 2023-12-08 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_solutions_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutions',
            name='climate_paramter',
        ),
    ]