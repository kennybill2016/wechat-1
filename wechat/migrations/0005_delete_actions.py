# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0004_actions_back'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Actions',
        ),
    ]
