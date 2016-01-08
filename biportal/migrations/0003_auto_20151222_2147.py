# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biportal', '0002_datatransjob_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatransjob',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 22, 13, 47, 37, 817355, tzinfo=utc)),
        ),
    ]
