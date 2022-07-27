from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from store_app.models import Cart


class ShoppingPaymentView(ListView):
    model = Cart
    template_name = 'payment_app/shopping-payment.html'
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(user__email=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Cart.objects.filter(user__email=self.request.user).count()
        return context


class ShoppingView(TemplateView):
    template_name = 'payment_app/shopping.html'


def payment_compelete_view(request):
    cart = Cart.objects.filter(user=request.user.id)
    price = sum([int(c.product.price)*int(c.quantity) for c in Cart.objects.filter(user__email=request.user)])
    cart.delete()
    return render(request, 'payment_app/shopping-complete-buy.html', {'price':price})


def payment_no_compelete_view(request):
    return render(request, 'payment_app/shopping-no-complete-buy.html')