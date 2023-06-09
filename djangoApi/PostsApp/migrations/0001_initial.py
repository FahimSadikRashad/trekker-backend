# Generated by Django 3.2 on 2022-11-05 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
                ('category_used', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AllPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Author', models.CharField(max_length=50)),
                ('datetime', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('likes', models.IntegerField()),
                ('imgLink', models.BooleanField()),
                ('imgOrVideoLink', models.URLField()),
                ('comments', models.IntegerField()),
                ('body', models.CharField(max_length=50)),
                ('catagory', models.ManyToManyField(to='PostsApp.Categories')),
            ],
        ),
    ]
