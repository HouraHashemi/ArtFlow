from typing import Any
from django.contrib import admin, messages
# from .models import Artwork, Category

# admin.site.register(Artwork)
# admin.site.register(Category)from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.models import LogEntry
from django.db.models.query import QuerySet
from .models import Artwork, Category
from django.utils.safestring import mark_safe
from django.utils.html import format_html, urlencode
from django.urls import reverse

admin.site.site_header = 'ArtFlow Administration'
admin.site.index_title = 'Admin Panel'



@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    actions = ['back_selling_state_to_defaulte']
    list_display = ['id', 'title', 'image_thumb', 'selling_state_mode', 'floor_price', 'categories_type']
    list_editable = ['floor_price']
    list_per_page = 10 
    list_select_related = ['artist']
    list_filter = ['categories', 'selling_state', 'created_at']
    # startswith for searching by first letter
    # adding i for making not sensitive to capital
    search_fields = ['artist__username__istartswith', 'title__istartswith']
    filter_horizontal = ['categories']


    @admin.display(ordering='selling_state_mode')
    def selling_state_mode(self, artwork):
        # app_model_page
        # makeing text link and navigate
        url = (
            reverse('admin:Artworks_artwork_changelist')
            + '?'
            + urlencode({
                'selling_state': str(artwork.selling_state)
            })
        )
        return format_html('<a href="{}">{}</a>', url, artwork.selling_state)


    @admin.display(ordering='categories_type')
    def categories_type(self, artwork):
        return [category.name for category in artwork.categories.all()]   
    
    
    def image_thumb(self, obj):
        # Display a thumbnail of the image in the admin
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />')
        else:
            return '(No image)'
    image_thumb.short_description = 'Image Thumbnail'  # Custom column header


    @admin.action(description='Back selling_state to not_sold')
    def back_selling_state_to_defaulte(self, request, queryset):
        updated_selling_state = queryset.update(selling_state='not_sold')
        self.message_user(
            request,
            f'{updated_selling_state} artworks were succesfully updated.',
            messages.WARNING
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
