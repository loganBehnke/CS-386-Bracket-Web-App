from django import forms
from django.contrib.auth import get_user_model
from .models import Player

User = get_user_model()

class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'gameName',
        ]

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class RigesterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RigesterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

