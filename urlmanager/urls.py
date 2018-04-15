from django.urls import path, include

from .views import AddUrl, ShortUrlRedirect


app_name = 'urlmanager'

urlpatterns = [
    path('', AddUrl.as_view(), name='add_url'),
    path('<short_url_path>/', ShortUrlRedirect.as_view(), name='redirect'),
]
