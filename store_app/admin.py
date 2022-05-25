from django.contrib import admin
from .models import Brand, Category, MobileProduct, Comment, Cart


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(MobileProduct)
admin.site.register(Comment)
admin.site.register(Cart)
