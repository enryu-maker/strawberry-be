# Generated by Django 4.2.15 on 2024-08-25 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
    ]
