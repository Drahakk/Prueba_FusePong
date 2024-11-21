from django import forms 
from .models import D, T
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass

class DForm(forms.ModelForm):
    class Meta:
        model = D
        fields = '__all__'

class TForm(forms.ModelForm):
    class Meta:
        model = T
        fields = '__all__'