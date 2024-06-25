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
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'required': 'true', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'required': 'true'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'marital_status': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'nationality': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'sector': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'cell': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'village': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'relative': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'relationship': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
        }
