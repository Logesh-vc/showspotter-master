# Generated by Django 5.0.3 on 2024-03-28 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_booking_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='session',
        ),
    ]
