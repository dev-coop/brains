# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='secret',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
