# artwork/serializers.py
from rest_framework import serializers
from .models import Artwork, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ArtworkSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    class Meta:
        model = Artwork
        fields = ['id', 'artist', 'title', 'description', 'image', 'floor_price', 'created_at', 'selling_state', 'floor_price', 'categories']


