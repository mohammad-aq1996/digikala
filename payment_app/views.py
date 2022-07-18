from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from store_app.models import Cart
from django.db.models.aggregates import Count
from django.db.models import F

class ShoppingPaymentView(ListView):
    model = Cart
    template_name = 'payment_app/shopping-payment.html'
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(user__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Cart.objects.filter(user__username=self.request.user).count()
        return context


class ShoppingView(TemplateView):
    template_name = 'payment_app/shopping.html'


def payment_compelete_view(request):
    cart = Cart.objects.filter(user=request.user.id)
    cart.delete()
    return render(request, 'payment_app/shopping-complete-buy.html')


def payment_no_compelete_view(request):
    return render(request, 'payment_app/shopping-no-complete-buy.html')