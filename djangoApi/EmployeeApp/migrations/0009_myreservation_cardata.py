# Generated by Django 3.2.10 on 2022-11-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0008_myreservation_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='myreservation',
            name='cardata',
            field=models.IntegerField(default=0),
        ),
    ]