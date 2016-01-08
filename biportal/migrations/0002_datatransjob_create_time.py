# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatransjob',
            name='create_time',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
