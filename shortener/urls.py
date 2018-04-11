from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path(f'{settings.ADMIN_URL_PATH}/', admin.site.urls),
    path('', include('urlmanager.urls', namespace='urlmanager')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
