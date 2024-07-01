from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.models import LogEntry
from .models import User, Customer  # Ensure User is correctly imported


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
    list_select_related = ['user']

    # needs functions in model to recognize these
    list_display = ['first_name', 'last_name', 'bio']
    # to decreaseing requests
    ordering = ['user__first_name', 'user__last_name']
