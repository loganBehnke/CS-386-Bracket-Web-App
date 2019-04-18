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

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class JoinBracketForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = [
            'teams'
        ]
    def __init__(self, user=None, *args, **kwargs):
        super(JoinBracketForm, self).__init__(*args, **kwargs)
        bracket = kwargs['instance']
        self.fields['teams'].queryset = Team.objects.all().exclude(bracket= bracket).filter(teamCaptin=user)
