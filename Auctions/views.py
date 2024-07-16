from django.shortcuts import render
from .models import Auction, Bid
from .serializers import AuctionSerializer, BidSerializer
from rest_framework import viewsets, status
from Artworks.models import Artwork



class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    # def get_queryset(self):
    #     return Artwork.objects.get_or_create(artist=self.request.user)
