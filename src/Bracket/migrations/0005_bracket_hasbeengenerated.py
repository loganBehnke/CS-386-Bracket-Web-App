# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bracket', '0004_remove_bracket_hasbeengenerated'),
    ]

    operations = [
        migrations.AddField(
            model_name='bracket',
            name='hasBeenGenerated',
            field=models.BooleanField(default=False),
        ),
    ]
