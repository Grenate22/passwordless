# Generated by Django 4.2.7 on 2023-12-20 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0006_alter_pin_email_alter_pin_otp_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 20, 8, 20, 59, 845691, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
