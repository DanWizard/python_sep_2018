# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='first_name',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='email',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='last_name',
            new_name='title',
        ),
    ]
