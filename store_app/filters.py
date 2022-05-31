from django.db import models 
from django import forms
import django_filters
from .models import MobileProduct


class MobileFilter(django_filters.FilterSet):
    CHOICES = (
        ("desc", "نزولی"),
        ("price-h2l", "قیمت نزولی"),
        ("price-l2h", "قیمت صعودی"),
    )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method="filter_by_order")

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    ava = django_filters.BooleanFilter(label='available', method='filter_by_available', widget=forms.CheckboxInput)

    def filter_by_order(self, queryset, name, value):
        if value == 'desc':
            expression = '-created'
        elif value == 'price-h2l':
            expression = '-price'
        elif value == 'price-l2h':
            expression = 'price'
        return queryset.order_by(expression)

    def filter_by_available(self, queryset, name, value):
        if value == True:
            return queryset.filter(**{'available':True})
        else:
            return queryset