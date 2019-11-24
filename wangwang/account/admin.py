from django.contrib import admin

from .models import Organization, User, Token


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'date_joined',
        'last_login',
        'organization',
        'sex',
    )
    list_filter = ('sex', 'organization', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'organization')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_name', )


@admin.register(Token)
class Tokendmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'created',
        'expired',
        'token',
    )
    ordering = ('id', )
