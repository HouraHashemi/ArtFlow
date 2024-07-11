# artwork/serializers.py
from rest_framework import serializers
from .models import Artwork, Category


class ArtworkSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    class Meta:
        model = Artwork
        fields = ['id', 'artist' ,'title', 'description', 'image', 'floor_price', 'created_at', 'selling_state', 'categories']
        read_only_fields = ['artist']  # Ensure artist field is read-only


class SimpleArtworkSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()
    class Meta:
        model = Artwork
        fields = ['id', 'artist' ,'title', 'image',]
        read_only_fields = ['artist']  # Ensure artist field is read-only



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CustomerArtworkSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    class Meta:
        model = Artwork
        fields = ['id', 'artist' ,'title', 'description', 'image', 'floor_price', 'created_at', 'selling_state', 'floor_price', 'categories']
        read_only_fields = ['artist']  # Ensure artist field is read-only
