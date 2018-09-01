# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-01 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0002_student_iscoordinator'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='coordinator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='placement.Student'),
            preserve_default=False,
        ),
    ]
