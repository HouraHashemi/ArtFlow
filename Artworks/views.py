# artwork/views.py
from rest_framework import viewsets
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
