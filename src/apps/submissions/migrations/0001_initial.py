# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Participant')),
            ],
        ),
    ]
