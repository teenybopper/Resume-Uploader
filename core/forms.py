from django import forms
from .models import uploader


class uploaderform(forms.ModelForm):
    class Meta:
        model = uploader
        fields='__all__'
        label = {'name':'Full Name'}
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'job_city':forms.Select(attrs={'class':'form-select'})
        }