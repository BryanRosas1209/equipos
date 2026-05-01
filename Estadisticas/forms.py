from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_editor = forms.BooleanField(required=False, label="¿Es editor de estadísticas?")

    class Meta:
        model = User
        fields = ('username', 'email', 'is_editor')