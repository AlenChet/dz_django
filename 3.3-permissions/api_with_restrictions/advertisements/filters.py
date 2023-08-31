from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    status = filters.CharFilter(choices=Advertisement.STATUS_CHOICES)
    creator = filters.NumberFilter(field_name='creator')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
