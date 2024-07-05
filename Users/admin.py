from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.models import LogEntry
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import User, Customer  # Ensure User is correctly imported
from django.db.models import Count, Prefetch
from django.contrib.auth.models import Group
from django.db.models import Count, F, Q
from Artworks.models import Artwork
from django.contrib.contenttypes.admin import GenericTabularInline



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2",'email','first_name','last_name'),
            },
        ),
    )# first_name and last name are not in the model. so they are not mandetory.



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    # needs functions in model to recognize these
    list_display = ['user','first_name', 'last_name', 'bio', 'group', 'user_artworks_count']
    list_select_related = ['user']

    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'group__istartswith']

    @admin.display(ordering='group')
    def group(self, customer):
        return [group.name for group in customer.user.groups.all()]
    #     return customer.group_permissions
    

    @admin.display(ordering='user_artworks_count')
    def user_artworks_count(self, artwork):
        return artwork.artwork_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            artwork_count = Count('user_artworks')
        )


