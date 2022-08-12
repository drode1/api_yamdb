from django_filters import rest_framework as filters
from reviews.models import Title


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TitleFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__slug', lookup_expr='in')
    year = filters.NumberFilter()
    name = filters.CharFilter(lookup_expr='icontains')
    category = CharFilterInFilter(field_name='category__slug')

    class Meta:
        model = Title
        fields = ('genre', 'year', 'name', 'category')
