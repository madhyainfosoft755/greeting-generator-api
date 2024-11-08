from django import forms
from poster_templates.models import Festival, Client

class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['name']  # Only the 'name' field to add a new occasion
        labels = {
            'name': 'Occasion Name'
        }

      

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'logo', 'email', 'contact', 'website', 'tagline']
