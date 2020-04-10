from django import forms
from .models import Smiles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SmileForm(forms.ModelForm):
    class Meta:
        model = Smiles
        fields = ['smile_img']


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=200, required=True)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )
