from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-country-details', views.country_details, name='get-country-details'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
