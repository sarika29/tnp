# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='iscoordinator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='min_cgpa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
