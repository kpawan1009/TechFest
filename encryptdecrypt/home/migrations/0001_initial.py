# Generated by Django 4.2.7 on 2023-11-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('usn', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('marks1', models.IntegerField(default=0)),
                ('marks2', models.IntegerField(default=0)),
                ('marks3', models.IntegerField(default=0)),
                ('marks4', models.IntegerField(default=0)),
                ('marks5', models.IntegerField(default=0)),
                ('marks6', models.IntegerField(default=0)),
                ('marks7', models.IntegerField(default=0)),
            ],
        ),
    ]
