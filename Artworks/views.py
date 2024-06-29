# artwork/views.py
from rest_framework import viewsets

from .filters import ArtworkFilter
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['artist','title','categories']
    filterset_class = ArtworkFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
