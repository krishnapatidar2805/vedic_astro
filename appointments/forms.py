from django import forms
from .models import Appointment
import datetime


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'full_name', 'phone', 'email', 'date_of_birth', 'time_of_birth',
                  'place_of_birth', 'preferred_date', 'preferred_time', 'consultation_mode', 'message']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address (optional)'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_of_birth': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth'}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'consultation_mode': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Briefly describe your problem/question'}),
        }

    def clean_preferred_date(self):
        date = self.cleaned_data['preferred_date']
        if date < datetime.date.today():
            raise forms.ValidationError("Preferred date cannot be in the past.")
        return date
