
from django.contrib import admin
from django.urls import path
from restauracja import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservations/', views.reservations, name='reservations'),
    path('reviews/', views.reviews, name='reviews'),
]
