# Generated by Django 3.2.8 on 2021-11-23 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_addapartment_stno'),
    ]

    operations = [
        migrations.AddField(
            model_name='addapartment',
            name='expiredate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 11, 23, 23, 5, 32, 728423)),
        ),
        migrations.AddField(
            model_name='addapartment',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 11, 23, 23, 5, 32, 728423)),
        ),
    ]
