# Generated by Django 3.0.7 on 2020-06-30 01:03

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200629_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 18, 3, 49, 676121)),
        ),
        migrations.AlterField(
            model_name='settings',
            name='fps',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
