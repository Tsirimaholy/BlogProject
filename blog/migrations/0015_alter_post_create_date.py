# Generated by Django 3.2.7 on 2021-09-17 11:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 11, 55, 32, 499730, tzinfo=utc)),
        ),
    ]