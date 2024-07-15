from django.shortcuts import render
from .models import Auction, Bid
from .serializers import AuctionSerializer, BidSerializer
from rest_framework import viewsets, status


# Create your views here.
class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer



class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer