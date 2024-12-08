from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/',views.brand_list,name='brand_list'),
    path('cars/',views.car_list,name='car_list'),
]
