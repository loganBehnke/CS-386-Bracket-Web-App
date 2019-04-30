from django import forms
from django.contrib.auth.admin import User
from .models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
        ]


class JoinTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'players',
            'subs',
        ]
    