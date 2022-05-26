from .models import Cart
from django.shortcuts import render



def b(request):
    context = {
        'carts':Cart.objects.filter(user__username='mamali'),
        'total_price':sum([int(c.product.price) for c in Cart.objects.filter(user__username='mamali')])
    }
    return context

def c(request):
        return {'h':10}
