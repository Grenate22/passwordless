# Generated by Django 4.2.7 on 2023-12-20 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0007_alter_pin_otp_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 20, 8, 33, 12, 674392, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
