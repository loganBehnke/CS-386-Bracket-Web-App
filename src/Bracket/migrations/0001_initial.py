# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('minNumOfTeams', models.IntegerField(blank=True, default=4)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('hasBeenGenerated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team.Team')),
                ('team2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team.Team')),
                ('winningTeam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('matches', models.ManyToManyField(blank=True, to='Bracket.Match')),
            ],
        ),
        migrations.AddField(
            model_name='bracket',
            name='rounds',
            field=models.ManyToManyField(blank=True, to='Bracket.Round'),
        ),
        migrations.AddField(
            model_name='bracket',
            name='teams',
            field=models.ManyToManyField(blank=True, to='team.Team'),
        ),
    ]
