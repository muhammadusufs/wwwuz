# Generated by Django 4.2.7 on 2023-12-03 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_data_counter_data_unique_visitors_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApiKey',
        ),
    ]