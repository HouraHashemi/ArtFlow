# artwork/serializers.py
from rest_framework import serializers
from .models import Artwork, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ArtworkSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Artwork
        fields = ['id', 'artist', 'title', 'description', 'image', 'price', 'categories', 'created_at']
