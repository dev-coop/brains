# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20151217_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='dataset',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
