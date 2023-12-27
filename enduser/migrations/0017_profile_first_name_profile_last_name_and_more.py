# Generated by Django 4.2.7 on 2023-12-27 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0016_alter_pin_otp_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 27, 11, 3, 16, 298842, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
