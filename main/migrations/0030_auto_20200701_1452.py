# Generated by Django 3.0.7 on 2020-07-01 21:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20200701_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 21, 52, 26, 295074, tzinfo=utc)),
        ),
    ]