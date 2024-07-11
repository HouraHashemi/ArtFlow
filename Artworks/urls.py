# myartsite/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'admin-artworks-api', views.ArtworkViewSet,basename='admin-artworks')
router.register(r'categories-api', views.CategoryViewSet, basename='categories')
router.register(r'customer-artworks-api', views.CustomerArtworkViewSet, basename='customer-artworks')


urlpatterns = [
    path('', include(router.urls)),

]
