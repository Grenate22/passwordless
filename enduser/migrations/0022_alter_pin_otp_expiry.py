# Generated by Django 4.2.7 on 2024-02-13 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0021_alter_pin_otp_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 13, 13, 33, 9, 562913, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
