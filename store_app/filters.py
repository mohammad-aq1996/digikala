import django_filters
from .models import MobileProduct


class MobileFilter(django_filters.FilterSet):

    CHOICES = (
        ("desc", "نزولی"),
        ("price-h2l", "قیمت نزولی"),
        ("price-l2h", "قیمت صعودی"),
    )

    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method="filter_by_order")


    def filter_by_order(self, queryset, name, value):
        if value == 'desc':
            expression = '-created'
        elif value == 'price-h2l':
            expression = '-price'
        elif value == 'price-l2h':
            expression = 'price'
        return queryset.order_by(expression)
