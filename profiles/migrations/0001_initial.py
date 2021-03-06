# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-07 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0003_auto_20160128_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to=profiles.models.user_directory_path, verbose_name='Profile picture')),
                ('nick', models.SlugField(allow_unicode=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('joined_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
