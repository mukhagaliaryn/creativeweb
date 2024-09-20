from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', )
