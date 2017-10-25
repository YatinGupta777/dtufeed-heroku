# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20171009_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='event_datetime',
        ),
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='event_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
