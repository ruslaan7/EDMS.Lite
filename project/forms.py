from django import forms
from project.models import Document
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'description', 'document')
