
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

# from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls import url
# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    # path('users/', include('Users.urls')), 
    path('artworks/', include('Artworks.urls')), 
    # path('orders/', include('Orders.urls')), 
    # path('auctions/', include('Auctions.urls')), 

    # url(r'^$', schema_view)

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)