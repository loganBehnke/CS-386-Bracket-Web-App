from django import forms
from django.contrib.auth.admin import User

from .models import Bracket
from team.models import Team


class BracketCreateForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = [
            'name',
            'minNumOfTeams',
            'teams'
        ]


class JoinBracketForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = [
            'teams',
        ]