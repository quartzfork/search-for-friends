from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'first_name', 'last_name', 'telegram_username', 'age', 'gender', 'institution', 'interests']
