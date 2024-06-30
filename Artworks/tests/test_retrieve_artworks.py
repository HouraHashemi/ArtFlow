
from rest_framework.test import APIClient
from rest_framework import status
from Artworks.models import Artwork
import pytest
from model_bakery import baker
from django.utils import timezone



@pytest.mark.django_db
class TestRetrieveArtwork:

    @pytest.mark.skip
    def test_artwork_list_return_200(self, api_client):

        response = api_client.get('/artworks/artworks-api/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.skip
    def test_if_artwork_exist_returns_200(self, api_client):         
        artwork_instance = baker.make(Artwork)
        print(artwork_instance.__dict__)
        response = api_client.get('/artworks/artworks-api/{}/'.format(artwork_instance.id))
        assert response.status_code == status.HTTP_200_OK
        # assert response.data == {
        #     'id': artwork_instance.id,
        #     'artist': artwork_instance.artist,
        # }

