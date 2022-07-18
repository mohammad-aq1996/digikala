from .models import Cart
from django.shortcuts import render



def b(request):
    context = {
        'carts':Cart.objects.filter(user__username=request.user.username),
        'total_price':sum([int(c.product.price)*int(c.quantity) for c in Cart.objects.filter(user__username=request.user.username)])
    }
    return context

def c(request):
        return {'h':10}
