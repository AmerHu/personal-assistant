# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-13 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0004_auto_20161213_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_entry_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]