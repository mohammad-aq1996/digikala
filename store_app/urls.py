from django.urls import path
from .views import (ProductListView, ProductDetailView, CartListView, remove_from_cart,
                     ProductBrandListView)

app_name = 'store_app'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<slug:brand>/', ProductBrandListView.as_view(), name='product-brand-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('d/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    # path('product/srch/', ProductSearchView.as_view(), name='product-search'),
]