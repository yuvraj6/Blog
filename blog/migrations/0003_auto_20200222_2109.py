# Generated by Django 3.0.2 on 2020-02-22 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200216_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 15, 39, 10, 92372, tzinfo=utc)),
        ),
    ]
