# Generated by Django 3.0.5 on 2020-04-23 03:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20200422_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 3, 35, 38, 569144, tzinfo=utc)),
        ),
    ]
