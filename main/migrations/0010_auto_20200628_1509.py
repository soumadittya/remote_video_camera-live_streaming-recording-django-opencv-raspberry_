# Generated by Django 3.0.7 on 2020-06-28 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200628_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording', models.BooleanField(default=False)),
                ('path', models.CharField(default='videos/', max_length=200)),
                ('fps', models.CharField(choices=[('five', '5'), ('ten', '10'), ('twenty', '20'), ('twenty_five', '25'), ('thirty', '30')], default='twenty', max_length=11)),
            ],
        ),
        migrations.RemoveField(
            model_name='records',
            name='date',
        ),
        migrations.RemoveField(
            model_name='records',
            name='fps',
        ),
        migrations.RemoveField(
            model_name='records',
            name='path',
        ),
        migrations.AddField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 15, 9, 33, 958252)),
        ),
    ]
