# Generated by Django 3.2.7 on 2021-09-17 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 15, 17, 2, 620196, tzinfo=utc)),
        ),
    ]
