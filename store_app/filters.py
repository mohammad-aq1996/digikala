from django.db import models 
from django import forms
import django_filters
from .models import MobileProduct


class MobileFilter(django_filters.FilterSet):
    # class Meta:
    #     model = MobileProduct
        # fields = ['networks', 'available']
        # filter_overrides = {
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }

    CHOICES = (
        ("desc", "نزولی"),
        ("price-h2l", "قیمت نزولی"),
        ("price-l2h", "قیمت صعودی"),
    )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method="filter_by_order")

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    ava = django_filters.BooleanFilter(label='available', method='xx')

    def filter_by_order(self, queryset, name, value):
        if value == 'desc':
            expression = '-created'
        elif value == 'price-h2l':
            expression = '-price'
        elif value == 'price-l2h':
            expression = 'price'
        return queryset.order_by(expression)

    def xx(self, queryset, name, value):
        if value == True:
            return queryset.filter(**{'available':True})
        else:
            return queryset