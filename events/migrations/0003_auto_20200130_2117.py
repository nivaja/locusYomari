# Generated by Django 3.0.2 on 2020-01-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_locationimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='LocationImage',
            field=models.ImageField(upload_to='images'),
        ),
    ]