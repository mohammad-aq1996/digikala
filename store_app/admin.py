from django.contrib import admin
from .models import Brand, Category, Product, Comment, Cart


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Cart)
