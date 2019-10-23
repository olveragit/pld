from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'email']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password']
