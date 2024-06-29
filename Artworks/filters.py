from django_filters.rest_framework import FilterSet
from .models import Artwork


class ArtworkFilter(FilterSet):
    class Meta:
        model = Artwork
        fields = {
            'artist': ['exact'],
            'title': ['exact'],
            'floor_price': ['lt', 'gt'], 
        }