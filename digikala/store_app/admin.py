from django.contrib import admin
from .models import Brand, Category, Product, Comment, Cart


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}

class CommentAdmin(admin.TabularInline):
    model = Comment
    list_display = ['user', 'status']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['persian_title', 'price', 'category', 'count']
    inlines = [CommentAdmin]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


