from django.shortcuts import render, redirect
from django.views import View
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

class ShortUrlRedirect(View):

    def get(self, request, *args, **kwargs):
        short_url_path = kwargs['short_url_path']
        if short_url_path:
            try:
                url = Url.objects.get(short_url_path=short_url_path)
                if url is not None:
                    return redirect(url.get_full_url())
            except Url.DoesNotExist:
                # In order to prevent abuse, additional logic can be added here.
                # For example counting unsuccessful trials.
                # For now we'll go with silently redirecting to add url page.
                pass
        # If nonexistent short url or even arbitrary path is used,
        # silently redirect to page for adding URL
        return redirect('urlmanager:add_url')