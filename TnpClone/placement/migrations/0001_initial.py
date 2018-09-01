# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'submitted'), (2, 'onlineTest'), (3, 'selected')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MME', 'MME'), ('BIO', 'BIO')], default='CSE', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('min_cgpa', models.IntegerField()),
                ('branchOptions', models.ManyToManyField(blank=True, related_name='company', to='placement.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('regno', models.IntegerField(unique=True)),
                ('rollno', models.IntegerField(unique=True)),
                ('cgpa', models.IntegerField()),
                ('resume', models.FileField(upload_to=b'')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement.Branch')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement.Company'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement.Student'),
        ),
    ]
