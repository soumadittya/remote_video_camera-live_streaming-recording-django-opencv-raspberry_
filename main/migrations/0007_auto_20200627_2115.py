# Generated by Django 3.0.7 on 2020-06-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200627_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.CharField(default='20/06/27', max_length=14),
        ),
        migrations.AlterField(
            model_name='records',
            name='time',
            field=models.CharField(default='21:15:08', max_length=9),
        ),
    ]