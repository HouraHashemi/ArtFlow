from django.apps import AppConfig


class ArtworksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Artworks'

    def ready(self):
            import Artworks.signals  