# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='score',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]