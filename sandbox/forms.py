from django import forms
from django.contrib.auth.models import User

from sandbox.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('author', 'recipient', 'text', 'image',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password'}
