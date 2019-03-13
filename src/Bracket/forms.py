from django import forms
from django.contrib.auth.admin import User

from .models import Bracket
from RegisteredTeams.models import Team


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
            'teams',
        ]