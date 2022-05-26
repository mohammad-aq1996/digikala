from django.urls import path
from .views import MobileListView, MobileDetailView, CartListView, remove_from_cart, MobileBrandListView

app_name = 'store_app'

urlpatterns = [
    path('mobiles/', MobileListView.as_view(), name='mobile-list'),
    path('mobile/<slug:brand>/', MobileBrandListView.as_view(), name='mobile-brand-list'),
    path('mobile/<int:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('d/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    # path('D/<int:pk>/', D.as_view(), name='D'),

]