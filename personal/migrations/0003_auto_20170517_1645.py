# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-17 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='page',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
