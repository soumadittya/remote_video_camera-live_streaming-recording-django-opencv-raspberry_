from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ModifiedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']