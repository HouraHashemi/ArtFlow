# artwork/serializers.py
from rest_framework import serializers
from .models import Artwork, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

 

class ArtworkSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        many=True,
        slug_field='name'
    )

    artist = serializers.StringRelatedField()

    size = serializers.SerializerMethodField(method_name='artwork_size')
    def artwork_size(self, artwork: Artwork):
        return "{}x{}x{}".format(artwork.width, artwork.height, artwork.depth)

    class Meta:
        model = Artwork
        fields = ['id',
                   'artist',
                     'title',
                       'description',
                         'image',
                           'floor_price',
                             'created_at',
                               'selling_state',
                                 'categories',
                                   'size', 'height', 'width', 'depth',
                                   ]
        read_only_fields = ['artist']  # Ensure artist field is read-only
        extra_kwargs = {
            'height': {'write_only': True},
            'width': {'write_only': True},
            'depth': {'write_only': True}
        }
        



class SimpleArtworkSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer()
    artist = serializers.StringRelatedField()


    class Meta:
        model = Artwork
        fields = ['id',
                   'artist',
                     'title',
                       'image',]
        read_only_fields = ['artist']  # Ensure artist field is read-only


