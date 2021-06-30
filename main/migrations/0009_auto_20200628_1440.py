# Generated by Django 3.0.7 on 2020-06-28 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200628_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='fps',
            field=models.CharField(choices=[('five', '5'), ('ten', '10'), ('twenty', '20'), ('twenty_five', '25'), ('thirty', '30')], default='twenty', max_length=11),
        ),
        migrations.AddField(
            model_name='records',
            name='path',
            field=models.CharField(default='videos/', max_length=200),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 14, 40, 50, 270981)),
        ),
    ]
