# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180502_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]