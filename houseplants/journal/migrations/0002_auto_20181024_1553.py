# Generated by Django 2.1.2 on 2018-10-24 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 15, 53, 3, 861735, tzinfo=utc), verbose_name='publish date'),
        ),
    ]