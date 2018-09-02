# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import placement.models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0004_auto_20180902_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='user',
            new_name='student',
        ),
        migrations.AddField(
            model_name='application',
            name='attachment',
            field=models.FileField(default=1, unique=True, upload_to=placement.models.get_resume_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='file_name',
            field=models.CharField(default='xxx', max_length=100),
        ),
    ]
