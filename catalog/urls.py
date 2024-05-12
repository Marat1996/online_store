from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:slug>/', views.CategoryProductsView.as_view(), name='category_products'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='add_to_cart'),
]