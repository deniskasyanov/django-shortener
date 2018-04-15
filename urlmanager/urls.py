from django.urls import path, include

from .views import AddUrl


app_name = 'urlmanager'

urlpatterns = [
    path('', AddUrl.as_view(), name='add_url'),
]
