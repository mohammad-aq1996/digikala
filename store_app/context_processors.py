from .models import Cart
from django.shortcuts import render



def b(request):
    context = {
        'carts':Cart.objects.filter(user__email=request.user.email),
        'total_price':sum([int(c.product.price)*int(c.quantity) for c in Cart.objects.filter(user__email=request.user.email)])
    }
    return context

def c(request):
        return {'h':10}
