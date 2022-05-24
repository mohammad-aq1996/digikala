from types import ModuleType
from django.views.generic import ListView

from .models import Brand, Category, MobileProduct, Comment


class MobileListView(ListView):
    model = MobileProduct
    template_name = 'store_app/mobile-list.html'
    context_object_name = 'mobiles'