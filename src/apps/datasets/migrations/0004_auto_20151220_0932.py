# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 09:32
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0003_dataset_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file',
            field=s3direct.fields.S3DirectField(),
        ),
    ]
