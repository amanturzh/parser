# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xlsparse', '0004_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='create_date',
        ),
    ]
