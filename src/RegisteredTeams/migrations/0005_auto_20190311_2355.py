# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-11 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegisteredTeams', '0004_auto_20190311_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamCaptin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='player.Player'),
        ),
    ]
