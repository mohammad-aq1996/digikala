from re import template
from django.urls import path
from django.views.generic import TemplateView
from .views import ShoppingPaymentView, payment_compelete_view, payment_no_compelete_view, ShoppingView


app_name = 'payment_app'

urlpatterns = [
    path('shopping/payment/', ShoppingPaymentView.as_view(), name='shopping-payment'),
    path('shopping/payment/compelete/', payment_compelete_view, name='shopping-compelete'),
    path('shopping/payment/no/compelete/', payment_no_compelete_view, name='shopping-no-compelete'),
    path('shopping/', ShoppingView.as_view(), name="shopping")
]
