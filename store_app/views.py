from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Brand, Category, MobileProduct, Comment, Cart
from .forms import CommentForm


class MobileMixin:
    model = MobileProduct
    context_object_name = 'mobiles'


class MobileListView(MobileMixin, ListView):
    template_name = 'store_app/mobile-list.html'
    paginate_by = 1


class MobileBrandListView(MobileMixin, ListView):
    template_name = 'store_app/mobile-brand-list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(MobileBrandListView, self).get_context_data(**kwargs)
        context['mobiles'] = MobileProduct.objects.filter(brand__slug=self.kwargs['brand'])
        return context


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


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().__init__(**kwargs)
        context['carts'] = Cart.objects.filter(user__username='mamali')
        context['totla_price'] = sum([int(c.product.price) for c in Cart.objects.filter(user__username='mamali')])
        return context


class MobileSearchView(ListView):
    model = MobileProduct
    template_name = 'store_app/search.html'
    context_object_name = 'mobiles'
    paginate_by = 1

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qry = self.request.GET.get('q')
        return MobileProduct.objects.filter(Q(english_title__icontains=qry) | Q(persian_title__icontains=qry) | Q(review__icontains=qry))


def remove_from_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('store_app:cart'))
