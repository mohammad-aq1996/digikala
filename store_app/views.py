from email import message
from itertools import product
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Brand, Category, MobileProduct, Comment
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
