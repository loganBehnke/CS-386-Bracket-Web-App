# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bracket', '0002_match_winningteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='matchNum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
