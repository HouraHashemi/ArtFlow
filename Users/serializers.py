from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import Customer
from Artworks.serializers import ArtworkSerializer, SimpleArtworkSerializer
from Artworks.models import Artwork



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id',
                   'username',
                     'password',
                       'email',
                         'first_name',
                           'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id',
                   'username',
                     'email',
                       'first_name',
                         'last_name']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user_artworks = SimpleArtworkSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ['id',
                   'user_id',
                     'bio',
                       'user_artworks']





