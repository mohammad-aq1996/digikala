from django.urls import path
from .views import (ProductListView, MobileDetailView, CartListView, remove_from_cart,
                     ProductSearchView)

app_name = 'store_app'

urlpatterns = [
    path('products/<slug:slug>/', ProductListView.as_view(), name='product-list'),
    path('product/phone/<int:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('d/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('product/', ProductSearchView.as_view(), name='product-search'),

]