# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-21 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_trip_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='deactivated',
            field=models.CharField(default='N', max_length=255),
            preserve_default=False,
        ),
    ]
