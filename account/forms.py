from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'name', 'email', 'phone_number', 'id_number', 'gender', 'role', 'image', 'password1', 'password2'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': True}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number', 'required': True}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your ID Number', 'required': True}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': True}, choices=User.GENDER_CHOICES),
            'role': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))