# Generated by Django 3.0.5 on 2020-04-23 03:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200422_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 3, 34, 1, 566036, tzinfo=utc)),
        ),
    ]
