from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Url

class AddUrl(ModelForm):
    class Meta:
        model = Url
        fields = ['full_url',]

        widgets = {
            'full_url': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'})
        }

        labels = {
            'full_url': '',
        }



    def clean_full_url(self):
        full_url = self.cleaned_data['full_url']
        if not full_url.startswith('http'):
            full_url = f'http://{full_url}'
        return full_url
