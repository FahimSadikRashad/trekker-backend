# Generated by Django 3.2.10 on 2022-10-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterTable',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('UserPass', models.CharField(max_length=100)),
                ('UserEmail', models.CharField(max_length=100)),
            ],
        ),
    ]
