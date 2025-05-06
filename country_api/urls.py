from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
import country_api.core.urls as core_urls
import country_api.api.urls as api_urls

urlpatterns = [
    path('',include((core_urls, 'core'), namespace='core')),
    path('api/',include((api_urls, 'api'), namespace='api')),
]

urlpatterns += static(settings.STATIC_URL, document_root="static")

