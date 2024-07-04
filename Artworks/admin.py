from django.contrib import admin
# from .models import Artwork, Category

# admin.site.register(Artwork)
# admin.site.register(Category)from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.models import LogEntry
from .models import Artwork, Category
from django.utils.safestring import mark_safe
from django.utils.html import format_html, urlencode



# class ArtworkImageInline(admin.TabularInline):
#     model = Artwork
    
#     readonly_fields = ['thumbnail']
#     def thumbnail(self, instance):
#         if instance.image.name == '':
#             return format_html(f'<img src={instance.image.url} />')
#         else:
#             return ''


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['artist', 'title', 'image_thumb', 'selling_state', 'floor_price']
    filter_horizontal = ['categories']

    def image_thumb(self, obj):
        # Display a thumbnail of the image in the admin
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />')
        else:
            return '(No image)'
    image_thumb.short_description = 'Image Thumbnail'  # Custom column header
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
