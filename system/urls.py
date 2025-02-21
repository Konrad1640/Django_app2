
from django.contrib import admin
from django.urls import path
from restauracja import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('reservations/', views.reservations, name='reservations'),
    path('user-menu/', views.user_menu, name='user_menu'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('dish/delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
