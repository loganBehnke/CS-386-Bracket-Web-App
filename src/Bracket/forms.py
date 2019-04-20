from django import forms
from django.contrib.auth.admin import User
from django.http import HttpResponse, HttpResponseRedirect

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
            'teams'
        ]

    def __init__(self, user=None, *args, **kwargs):
        super(JoinBracketForm, self).__init__(*args, **kwargs)
        bracket = kwargs['instance']
        self.fields['teams'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['teams'].queryset = Team.objects.all().exclude(bracket= bracket).filter(teamCaptin=user)


    def save(self, commit=True):
        instance = super(JoinBracketForm, self).save(commit=False)
        teams = self.cleaned_data['teams']
        print(teams)
        for team in teams:
            instance.teams.add(team)
        instance.save()
        return instance
