from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]