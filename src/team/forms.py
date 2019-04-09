from django import forms
from django.contrib.auth.admin import User
from .models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
        ]

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class JoinTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'players',
            'subs',
        ]
    