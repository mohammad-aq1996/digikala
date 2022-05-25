from django.urls import path
from .views import MobileListView, MobileDetailView

app_name = 'store_app'

urlpatterns = [
    path('mobiles/', MobileListView.as_view(), name='mobile-list'),
    path('mobile/<int:pk>/', MobileDetailView.as_view(), name='mobile-detail'),
]