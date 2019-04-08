# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegisteredTeams', '0001_initial'),
        ('Bracket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winningTeam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='RegisteredTeams.Team'),
        ),
    ]