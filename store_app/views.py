from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Brand, Category, MobileProduct, Comment, Cart, LaptopProduct, LaptopComment
from .forms import CommentForm
from .filters import MobileFilter, LpatopFilter



class MobileListView(ListView):
    model = MobileProduct
    template_name = 'store_app/mobile-list.html'
    context_object_name = 'filter'
    paginate_by = 1

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qs = MobileProduct.objects.all()
        return MobileFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super(MobileListView, self).get_context_data(**kwargs)
        context['fltr'] = MobileFilter(self.request.GET, queryset=MobileProduct.objects.all())
        context['ordr'] = self.request.GET
        context['min_price'] = min([mobile.price for mobile in self.model.objects.all()])
        context['max_price'] = max([mobile.price for mobile in self.model.objects.all()])
        return context


class LaptopListView(ListView):
    model = LaptopProduct
    template_name = 'store_app/laptop-list.html'
    context_object_name = 'filter'
    paginate_by = 1

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qs = self.model.objects.all()
        return LpatopFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super(LaptopListView, self).get_context_data(**kwargs)
        context['fltr'] = LpatopFilter(self.request.GET, queryset=self.model.objects.all())
        context['ordr'] = self.request.GET
        context['min_price'] = min([int(laptop.price) for laptop in LaptopProduct.objects.all()])
        context['max_price'] = max([int(laptop.price) for laptop in LaptopProduct.objects.all()])
        return context


class MobileBrandListView(ListView):
    template_name = 'store_app/mobile-brand-list.html'
    model = MobileProduct
    context_object_name = 'filter'
    paginate_by = 1

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qs = MobileProduct.objects.filter(brand__slug=self.kwargs['brand'])
        return MobileFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fltr'] = MobileFilter(self.request.GET, queryset=self.get_queryset())
        context['ordr'] = self.request.GET
        context['brand'] = self.kwargs['brand']
        return context


class LaptopBrandListView(ListView):
    template_name = 'store_app/laptop-brand-list.html'
    model = LaptopProduct
    context_object_name = 'filter'
    paginate_by = 1

    def querystring(self):
        qs = self.request.GET.copy()
        qs.pop(self.page_kwarg, None)
        return qs.urlencode()

    def get_queryset(self):
        qs = self.model.objects.filter(brand__slug=self.kwargs['brand'])
        return LpatopFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fltr'] = LpatopFilter(self.request.GET, queryset=self.get_queryset())
        context['ordr'] = self.request.GET
        context['brand'] = self.kwargs['brand']
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
        qs = MobileProduct.objects.filter(Q(english_title__icontains=qry) | Q(persian_title__icontains=qry) | Q(review__icontains=qry))
        return MobileFilter(self.request.GET, queryset=qs).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fltr'] = MobileFilter(self.request.GET, queryset=self.get_queryset())
        context['ordr'] = self.request.GET
        context['qr'] = self.request.GET.get("q")
        
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
        if 'message' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                user = request.user
                message = form.cleaned_data['message']
                product = MobileProduct.objects.get(pk=self.kwargs['pk'])
                comment = Comment(user=user, message=message, product=product)
                comment.save()
            return redirect('store_app:mobile-detail', self.kwargs['pk'])
        else:
            product = MobileProduct.objects.get(id=self.kwargs['pk'])
            cart = Cart(product=product, user=request.user)
            cart.save()
            return redirect('store_app:cart')


class LaptopDetailView(DetailView):
    model = LaptopProduct
    template_name = 'store_app/laptop-detail.html'
    context_object_name = 'laptop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = LaptopComment.objects.filter(status='p', product=LaptopProduct.objects.get(pk=self.kwargs['pk']))
        return context

    def post(self, request, **kwargs):
        if 'message' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                user = request.user
                message = form.cleaned_data['message']
                product = self.model.objects.get(pk=self.kwargs['pk'])
                comment = LaptopComment(user=user, message=message, product=product)
                comment.save()
            return redirect('store_app:laptop-detail', self.kwargs['pk'])
        else:
            product = self.model.objects.get(id=self.kwargs['pk'])
            cart = Cart(product=product, user=request.user)
            cart.save()
            return redirect('store_app:cart')


class CartListView(LoginRequiredMixin, ListView):
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
        context = super().get_context_data(**kwargs)
        context['mobiles'] = MobileProduct.objects.all()[:7]
        return context



def remove_from_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return HttpResponseRedirect(reverse('store_app:cart'))
