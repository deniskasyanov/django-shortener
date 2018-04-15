from django.forms import ModelForm

from .models import Url

class AddUrl(ModelForm):
    class Meta:
        model = Url
        fields = ['full_url',]

    def clean_full_url(self):
        full_url = self.cleaned_data['full_url']
        if not full_url.startswith('http'):
            full_url = f'http://{full_url}'
        return full_url
