# Generated by Django 3.0.8 on 2020-08-02 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200801_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.date(2020, 8, 2)),
        ),
    ]
