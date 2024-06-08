from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from .models import User, Province


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'emial')}),
        (_('Permissions'), {'fields' :('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'friends':('username', 'phone_number', 'password1', 'password2'),
        }),
    )