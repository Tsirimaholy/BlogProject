# Generated by Django 3.2.7 on 2021-09-16 13:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 13, 24, 24, 311160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 13, 24, 24, 310562, tzinfo=utc)),
        ),
    ]
