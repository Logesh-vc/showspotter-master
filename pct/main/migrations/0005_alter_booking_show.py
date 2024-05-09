# Generated by Django 5.0.3 on 2024-03-28 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_user'),
        ('main', '0004_alter_booking_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_screen', to='dashboard.show'),
        ),
    ]
