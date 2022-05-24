from django.urls import path
from .views import MobileListView

app_name = 'store_app'

urlpatterns = [
    path('mobiles/', MobileListView.as_view(), name='mobile-list'),
]