# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-23 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170128_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
