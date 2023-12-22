# Generated by Django 4.2.7 on 2023-11-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email_verification_sent_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email_verification_token',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email_verified',
        ),
        migrations.AddField(
            model_name='customuser',
            name='confirmation_attempts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
