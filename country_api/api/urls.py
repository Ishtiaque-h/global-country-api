from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('get-all-countries/', views.CountryList.as_view(), name='all-countries'),
    path('get-specific-county/<int:pk>/', views.CountryDetails.as_view(), name='get-specific-county'),
]

