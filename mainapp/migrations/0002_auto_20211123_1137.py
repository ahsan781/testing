# Generated by Django 3.2.8 on 2021-11-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addapartment',
            name='Phone',
            field=models.CharField(default='1', max_length=800),
        ),
        migrations.AddField(
            model_name='addapartment',
            name='renter',
            field=models.CharField(default='1', max_length=800),
        ),
        migrations.AddField(
            model_name='addapartment',
            name='share',
            field=models.IntegerField(default='1'),
        ),
    ]
