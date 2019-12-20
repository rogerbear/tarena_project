# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20180503_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicate_date',
            field=models.DateField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=50, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=20, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=20, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(verbose_name='网址'),
        ),
        migrations.AddField(
            model_name='wife',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Author'),
        ),
    ]