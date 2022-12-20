from django.forms import ModelForm
from .models import Character
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CharacterForm(ModelForm):

    class Meta:
        model = Character
        exclude = ('user',)


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
