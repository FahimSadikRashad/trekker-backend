# Generated by Django 3.2.10 on 2022-10-23 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='cover',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
