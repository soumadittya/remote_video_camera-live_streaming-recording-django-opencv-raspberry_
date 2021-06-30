# Generated by Django 3.0.7 on 2020-06-29 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200629_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 3, 14, 43, 479478)),
        ),
        migrations.AlterField(
            model_name='settings',
            name='fps',
            field=models.CharField(choices=[('five', '5'), ('ten', '10'), ('twenty', '20'), ('twenty_five', '25'), ('thirty', '30')], max_length=11),
        ),
    ]
