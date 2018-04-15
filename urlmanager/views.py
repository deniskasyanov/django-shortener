from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Url
from .forms import AddUrl


class AddUrl(FormView):

    template_name = 'urlmanager/add_url.html'
    form_class = AddUrl
    success_url = ''

    def form_valid(self, form):
        full_url = form.cleaned_data['full_url']
        obj, created = Url.objects.get_or_create(full_url=full_url)
        return render(self.request, 'urlmanager/display_short_url.html', {'short_url': obj.get_short_url()})
