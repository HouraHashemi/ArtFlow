
from django.contrib import admin
from django.urls import include, path

# from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls import url
# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    path('users-api/', include('Users.urls')), 
    path('artworks-api/', include('Artworks.urls')), 
    path('orders-api/', include('Orders.urls')), 
    path('auctions-api/', include('Auctions.urls')), 

    # url(r'^$', schema_view)

]
