
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ETL.Urls.admin import urlpatterns as admin_urls
from ETL.Urls.debug_toolbar import urlpatterns as toolbar_urls
from ETL.Urls.swagger import urlpatterns as swagger_urls
from ETL.Urls.core import urlpatterns as core_urls


urlpatterns = []


urlpatterns.extend(admin_urls)
urlpatterns.extend(toolbar_urls)
urlpatterns.extend(swagger_urls)
urlpatterns.extend(core_urls)


urlpatterns += [
    path('auth/', include('dj_rest_auth.urls')), 
    path('auth/registration/', include('dj_rest_auth.registration.urls')), 
    path('auth/accounts/', include('allauth.urls')), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if hasattr(settings, 'MEDIA_URL_2'):
        urlpatterns += static(settings.MEDIA_URL_2, document_root=settings.MEDIA_ROOT)
