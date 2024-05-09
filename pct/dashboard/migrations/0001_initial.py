# Generated by Django 5.0.3 on 2024-03-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='theatre_manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=1000)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]