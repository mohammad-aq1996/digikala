from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Brand, Category, Product, Comment, Cart, Product
from .forms import CommentForm
from .filters import ProductFilter
from itertools import chain
import operator
from operator import attrgetter
from django.db.models import Max, Min


class ProductListView(ListView):
    model = Product
    template_name = 'store_app/product-list.html'
    context_object_name = 'filter'
    paginate_by = 10

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        if self.kwargs['slug'] == 'phone':
            qs = self.model.objects.filter(category__title='phone')
            return ProductFilter(self.request.GET, queryset=qs).qs
        elif self.kwargs['slug'] == 'laptop':
            qs = self.model.objects.filter(category__title='laptop')
            return ProductFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fltr'] = ProductFilter(self.request.GET, queryset=self.model.objects.all())
        context['ordr'] = self.request.GET
        context['min_price'] = min([product.price for product in self.model.objects.all()])
        context['max_price'] = max([product.price for product in self.model.objects.all()])
        context['brand'] = Brand.objects.all()
        return context


class ProductSearchView(ListView):
    template_name = 'store_app/search.html'
    context_object_name = 'products'
    paginate_by = 12

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qry = self.request.GET.get('q')
        qs = Product.objects.filter(Q(english_title__icontains=qry) | Q(persian_title__icontains=qry) | Q(review__icontains=qry))
        return ProductFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordr'] = self.request.GET
        context['qr'] = self.request.GET.get("q")
        context['fltr'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['ordr'] = self.request.GET
        context['min_price'] = min([product.price for product in self.get_queryset()])
        context['max_price'] = max([product.price for product in self.get_queryset()])
        context['brand'] = Brand.objects.all()
        return context


class MobileDetailView(DetailView):
    model = Product
    template_name = 'store_app/mobile-detail.html'
    context_object_name = 'mobile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(status='p', product=Product.objects.get(pk=self.kwargs['pk']))
        return context

    def post(self, request, **kwargs):
        if 'message' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                user = request.user
                message = form.cleaned_data['message']
                product = Product.objects.get(pk=self.kwargs['pk'])
                comment = Comment(user=user, message=message, product=product)
                comment.save()
            return redirect('store_app:product-detail', self.kwargs['pk'])
        else:
            if not request.user.is_authenticated:
                return redirect('accounts_app:login')
            product = Product.objects.get(id=self.kwargs['pk'])
            if Cart.objects.filter(product=product, user=request.user).exists():
                cart = Cart.objects.get(product=product, user=request.user)
                cart.quantity = cart.quantity + 1
                cart.save()
            else:
                Cart.objects.create(product=product, user=request.user)

            return redirect('store_app:cart')


class LaptopDetailView(DetailView):
    model = Product
    template_name = 'store_app/laptop-detail.html'
    context_object_name = 'laptop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(status='p', product=Product.objects.get(pk=self.kwargs['pk']))
        return context

    def post(self, request, **kwargs):
        if 'message' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                user = request.user
                message = form.cleaned_data['message']
                product = Product.objects.get(pk=self.kwargs['pk'])
                comment = Comment(user=user, message=message, product=product)
                comment.save()
            return redirect('store_app:product-detail', self.kwargs['pk'])
        else:
            if not request.user.is_authenticated:
                return redirect('accounts_app:login')
            product = Product.objects.get(id=self.kwargs['pk'])
            if Cart.objects.filter(product=product, user=request.user).exists():
                cart = Cart.objects.get(product=product, user=request.user)
                cart.quantity = cart.quantity + 1
                cart.save()
            else:
                Cart.objects.create(product=product, user=request.user)

            return redirect('store_app:cart')


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'store_app/cart.html'
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(user__username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totla_count'] = Cart.objects.filter(user__username=self.request.user).count()
        print(context)
        return context


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:7]
        return context



def remove_from_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('store_app:cart'))

