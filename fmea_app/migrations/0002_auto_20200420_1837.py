# Generated by Django 3.0.5 on 2020-04-20 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fmea_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmea_record',
            name='Rev_Date',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='fmea_record',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 20, 13, 7, 50, 922637, tzinfo=utc)),
        ),
    ]
