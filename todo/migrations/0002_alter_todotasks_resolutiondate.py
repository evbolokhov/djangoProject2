# Generated by Django 4.0.4 on 2022-05-31 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotasks',
            name='resolutionDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 1, 23, 12, 15, 283190), verbose_name='Дата выполнения'),
        ),
    ]
