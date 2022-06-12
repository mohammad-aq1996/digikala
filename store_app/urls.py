from django.urls import path
from .views import (MobileListView, MobileDetailView, CartListView, remove_from_cart,
                     MobileBrandListView, MobileSearchView, LaptopListView, 
                     LaptopBrandListView, LaptopDetailView)

app_name = 'store_app'

urlpatterns = [
    path('mobiles/', MobileListView.as_view(), name='mobile-list'),
    path('laptops/', LaptopListView.as_view(), name='laptop-list'),
    path('mobile/<slug:brand>/', MobileBrandListView.as_view(), name='mobile-brand-list'),
    path('laptop/<slug:brand>/', LaptopBrandListView.as_view(), name='laptop-brand-list'),
    path('mobiles/<int:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
    path('lap/<int:pk>/', LaptopDetailView.as_view(), name='laptop-detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('d/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('mob/sr/', MobileSearchView.as_view(), name='mobile-search'),
]