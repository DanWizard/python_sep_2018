# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-18 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]