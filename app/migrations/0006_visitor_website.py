# Generated by Django 4.2.7 on 2023-12-04 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_website_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.website'),
        ),
    ]
