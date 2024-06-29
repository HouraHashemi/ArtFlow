# myartsite/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ArtworkViewSet, CategoryViewSet
from . import views

router = DefaultRouter()
router.register(r'artworks', views.ArtworkViewSet)
# router.register(r'categories', views.CategoryViewSet)


urlpatterns = [
    # path('', views.ArtworkViewSet, name='testing'),  # Example URL pattern for the index view

    path('', include(router.urls)),
]
