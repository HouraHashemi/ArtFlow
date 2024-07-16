# artwork/views.py
from rest_framework import viewsets

from .filters import ArtworkFilter
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly, ViewCustomerArtworkPermission
from rest_framework.permissions import IsAuthenticated


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.select_related('owner').all()
    serializer_class = ArtworkSerializer

    # custom filter | filterset_fields = ['owner','title','categories']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtworkFilter

    permission_classes = [IsAdminOrReadOnly]




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]




class CustomerArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.select_related('owner').all()
    serializer_class = ArtworkSerializer

    def get_queryset(self):
        return Artwork.objects.filter(owner=self.request.user)

    # custom filter | filterset_fields = ['owner','title','categories']
    filter_backends = [DjangoFilterBackend]
    # permission_classes = [ViewCustomerArtworkPermission]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
