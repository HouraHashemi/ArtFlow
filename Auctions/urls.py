# myartsite/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ArtworkViewSet, CategoryViewSet
from . import views

router = DefaultRouter()
# router.register(r'auctions', views.AuctionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
