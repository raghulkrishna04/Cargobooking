from django import forms
from .models import Booking
from django.contrib.auth.forms import AuthenticationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pickup_location', 'drop_location', 'date', 'lorry_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))