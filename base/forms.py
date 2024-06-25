from django import forms
from base.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'name',
            'dob',
            'image',
            'gender',
            'marital_status',
            'nationality',
            'id_number',
            'province',
            'district',
            'sector',
            'cell',
            'village',
            'phone_number',
            'relative',
            'relationship',
        ]
        widgets = {
            'name': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your name'}),
            'dob': forms.DateInput(attrs={ 'class': 'form-control',  'required': 'true',  'type': 'date',  'placeholder': 'Enter your date of birth'}),
            'image': forms.FileInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Upload your image'}),
            'gender': forms.Select(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Select your gender'}),
            'marital_status': forms.Select(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Select your marital status'}),
            'nationality': forms.Select(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Select your nationality'}),
            'id_number': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your ID number'}),
            'province': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your province'}),
            'district': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your district'}),
            'sector': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your sector'}),
            'cell': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your cell'}),
            'village': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your village'}),
            'phone_number': forms.TextInput(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Enter your phone number'}),
            'relative': forms.Select(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Select your relative'}),
            'relationship': forms.Select(attrs={ 'class': 'form-control',  'required': 'true',  'placeholder': 'Select your relationship'}),
        }

