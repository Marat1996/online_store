from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]