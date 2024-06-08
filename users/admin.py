from django.contrib import admin
from django.utils.translation import ugettext_lazy as _ 
from .models import User, Province
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


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
    list_display = ('username', 'phone_number', 'email', 'is_staff')
    search_fields =('username__exact',)
    ordering = ('-id')
    
    def get_serach_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filters(phone_number = search_term_as_int)
        return queryset, may_have_duplicates

admin.site.unregister(Group)
admin.site.register(Province)
admin.site.register(User, MyUserAdmin)
# admin.site.register(Site)