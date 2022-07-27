from django import forms
import django_filters


class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ("desc", "نزولی"),
        ("price-h2l", "قیمت نزولی"),
        ("price-l2h", "قیمت صعودی"),
    )
    BRAND_CHOICES = (
        ("1", "apple"),
        ("2", "samsung"),
        ("3", "xiaomi"),
        ("4", "asus"),
        ("5", "lenovo"),
    )
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method="filter_by_order")

    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    ava = django_filters.BooleanFilter(label='available', method='filter_by_available', widget=forms.CheckboxInput)

    brand = django_filters.MultipleChoiceFilter(label='brand' ,choices=BRAND_CHOICES)

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
            return queryset.filter(count__gt=0)
        else:
            return queryset