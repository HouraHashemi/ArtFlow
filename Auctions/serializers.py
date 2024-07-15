# artwork/serializers.py
from rest_framework import serializers
from .models import Auction, Bid


class AuctionSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()
    # artwork = serializers.StringRelatedField()

    class Meta:
        model = Auction
        fields = ['id',
                   'artwork',
                     'start_time',
                       'end_time',
                         'collector',
                           'bids']


class BidSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()

    

    class Meta:
        model = Bid
        fields = ['id',
                   'artwork',
                     'bidder',
                       'data',
                         'bid_price',
                           'is_valid']
