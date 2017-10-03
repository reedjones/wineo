# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-07 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import wines.models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0003_auto_20170707_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='label',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=wines.models.wine_directory_path),
        ),
    ]
