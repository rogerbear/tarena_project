# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-04 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20180503_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Publisher'),
        ),
    ]
