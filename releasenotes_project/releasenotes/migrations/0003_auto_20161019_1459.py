# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-19 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releasenotes', '0002_auto_20161019_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasenote',
            name='language',
            field=models.CharField(default='', max_length=7),
        ),
    ]
