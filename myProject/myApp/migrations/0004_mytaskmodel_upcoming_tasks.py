# Generated by Django 4.2.6 on 2024-02-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_custom_user_otp_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytaskmodel',
            name='upcoming_tasks',
            field=models.BooleanField(default=True),
        ),
    ]
