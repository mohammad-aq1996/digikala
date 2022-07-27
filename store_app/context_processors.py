from .models import Cart


def cart_context(request):
    context = {
        
        'carts':Cart.objects.filter(user__email=request.user),
        'total_price':sum([int(c.product.price)*int(c.quantity) for c in Cart.objects.filter(user__email=request.user)])
    }
    return context
