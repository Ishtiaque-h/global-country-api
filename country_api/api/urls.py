from django.urls import path, include
from . import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('get-all-countries/', views.CountryList.as_view(), name='all-countries'),
    path('get-specific-country/<int:pk>/', views.CountryDetails.as_view(), name='get-specific-country'),
    path('save-country-data/', views.SaveCountry.as_view(), name='save-country-data'),
    path('update-country-data/<int:pk>/', views.UpdateCountry.as_view(), name='update-country-data'),
    path('delete-specific-country/<int:pk>/', views.DeleteCountry.as_view(), name='delete-specific-country'),
    path('get-countries-with-region/', views.CountryListWithRegion.as_view(), name='get-countries-with-region'),
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    
]

