from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Brand, Category, MobileProduct, Comment, Cart
from .forms import CommentForm


class MobileListView(ListView):
    model = MobileProduct
    template_name = 'store_app/mobile-list.html'
    context_object_name = 'mobiles'


class MobileDetailView(DetailView):
    model = MobileProduct
    template_name = 'store_app/single-product.html'
    context_object_name = 'mobile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(status='p', product=MobileProduct.objects.get(pk=self.kwargs['pk']))
        return context

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            message = form.cleaned_data['message']
            product = MobileProduct.objects.get(pk=self.kwargs['pk'])
            comment = Comment(user=user, message=message, product=product)
            comment.save()
        return redirect('store_app:mobile-detail', self.kwargs['pk'])


class CartListView(ListView):
    model = Cart
    template_name = 'store_app/cart.html'
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(user__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totla_price'] = sum([int(c.product.price) for c in Cart.objects.filter(user__username='mamali')])
        context['totla_count'] = Cart.objects.filter(user__username=self.request.user).count()
        return context


# class D(DeleteView):
#     model = Cart
#     template_name = 'store_app/cart.html'
#     success_url = reverse_lazy('store_app:cart')


def remove_from_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('store_app:cart'))
