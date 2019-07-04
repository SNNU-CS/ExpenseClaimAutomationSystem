from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'organization', 'avatar'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'organization', 'is_staff', 'is_active', 'avatar')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'organization')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'organization')


admin.site.register(User, MyUserAdmin)
