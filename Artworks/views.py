# artwork/views.py
from rest_framework import viewsets

from .filters import ArtworkFilter
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly



class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

    # custom filter | filterset_fields = ['artist','title','categories']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter

    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]
