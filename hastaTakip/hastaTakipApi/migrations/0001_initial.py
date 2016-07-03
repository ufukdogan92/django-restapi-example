# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('doctor_lname', models.CharField(max_length=25)),
                ('doctor_email', models.EmailField(max_length=40)),
                ('doctor_gender', models.CharField(choices=[('K', 'Kadin'), ('E', 'Erkek')], max_length=1)),
                ('doctor_phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Doktor Profili',
                'verbose_name_plural': 'Doktor Profilleri',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=25)),
                ('patient_lname', models.CharField(max_length=25)),
                ('patient_email', models.EmailField(max_length=40)),
                ('patient_gender', models.CharField(choices=[('K', 'Kadin'), ('E', 'Erkek')], max_length=1)),
                ('patient_phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Hasta Profili',
                'verbose_name_plural': 'Hasta Profilleri',
            },
        ),
    ]
