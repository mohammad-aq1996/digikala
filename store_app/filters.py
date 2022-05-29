import django_filters
from .models import MobileProduct


class MobileFilter(django_filters.FilterSet):

    CHOICES = (
        ("asc", "صعودی"),
        ("desc", "نزولی")
    )

    ordering = django_filters.ChoiceFilter(label="Ordering", choices=CHOICES, method="filter_by_order")
    class Meta:
        model = MobileProduct
        fields = {
            'english_title': ['icontains']
            }

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'asc' else '-created'
        return queryset.order_by(expression)
