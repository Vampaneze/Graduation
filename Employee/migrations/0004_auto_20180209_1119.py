# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-09 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20180207_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default='', error_messages={'unique': 'نام دپارتمان تکراری است'}, max_length=30, unique=True),
        ),
    ]
