from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from .models import Customer
from Artworks.serializers import CustomerArtworkSerializer



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']



class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    # def create(self, validated_data):
    #     u_id = self.context['u_id']
    #     return Customer.objects.create(u_id)
        

    # user_artwork = CustomerArtworkSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'bio']
        # fields = ['id', 'user_id', 'bio', 'user_artwork']

