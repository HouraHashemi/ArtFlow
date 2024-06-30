
# semd reqiest to server
from rest_framework.test import APIClient
from rest_framework import status
from Artworks.models import Artwork, Category
import pytest
from model_bakery import baker
from Artworks.serializers import ArtworkSerializer
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def create_artwork(api_client):
    def do_create_artwrok(artwork):
        response = api_client.post('/artworks/artworks-api/', artwork)
    return do_create_artwrok


@pytest.mark.django_db
class TestCreateArtwork:


    @pytest.mark.skip
    def test_create_new_artwork_return_201(self, api_client):
        image_content = b'a fake image file content'
        image = SimpleUploadedFile(name='test_image.jpg', content=image_content, content_type='image/jpeg')
        artwork_data = {
            "id": 1,
            "artist": "Noura",
            "title": "Polar Bear",
            "description": "A bear wrapped in string of little light.",
            "image": image,
            "floor_price": 10.0,
            "created_at": timezone.now,
            "selling_state": "not_sold",
            "categories": [
                1,
                2
            ]
        }
        artwork = Artwork.objects.create(artwork_data)

        response = api_client.post('/artworks/artworks-api/', artwork)
        assert response.status_code == status.HTTP_201_CREATED


    @pytest.mark.skip
    def test_delete_an_artwork_return_201(self, api_client):
        artwork_instance = baker.make(Artwork)
        response = api_client.delete('/artworks/artworks-api/{}/'.format(artwork_instance.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    @pytest.mark.skip
    def test_put_an_artwork_return_200(self, api_client):
        artwork_instance = baker.make(Artwork)
        updated_data = {
            'title': 'Updated Title',
            'artist': 'Updated Artist',
        }
        response = api_client.put('/artworks/artworks-api/{}/'.format(updated_data.id), )
        assert response.status_code == status.HTTP_200_OK


    @pytest.mark.skip
    def test_patch_an_artwork_return_200(self, api_client):
        artwork_instance = baker.make(Artwork)
        updated_data = {
            'title': 'Updated Title',
            'artist': 'Updated Artist',
        }
        response = api_client.put('/artworks/artworks-api/{}/'.format(artwork_instance.id), updated_data)
        assert response.status_code == status.HTTP_200_OK



