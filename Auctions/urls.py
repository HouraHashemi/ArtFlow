# myartsite/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'auctions-api', views.AuctionViewSet, basename='auctions')
router.register(r'bids-api', views.BidViewSet, basename='bids')


urlpatterns = [
    path('', include(router.urls)),
]
