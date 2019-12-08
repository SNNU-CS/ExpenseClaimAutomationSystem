from django.contrib import admin

from .models import Organization, Token, User, Role


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
        'roles',
    )
    list_filter = ('sex', 'organization', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'organization')

    def roles(self, obj):
        return [_ for _ in obj.user_roles.all()]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'org_name', 'users')

    def users(self, obj):
        return [_.username for _ in obj.organization_users.all()]


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


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    ordering = ('id', )

    def user(self, obj):
        return [_.username for _ in obj.users.all()]
