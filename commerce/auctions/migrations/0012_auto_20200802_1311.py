# Generated by Django 3.0.8 on 2020-08-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200802_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
