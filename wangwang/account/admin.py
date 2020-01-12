from django.contrib import admin, messages
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from .forms import PasswordChangeForm, UserCreationForm
from .models import Organization, Role, Token, User


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
    form = UserChangeForm
    add_form = UserCreationForm
    change_user_password_template = None
    change_password_form = PasswordChangeForm

    def roles(self, obj):
        return [_ for _ in obj.user_roles.all()]

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def get_urls(self):
        return [
            path(
                '<id>/password/',
                self.admin_site.admin_view(self.user_change_password),
                name='user_password_change',
            ),
        ] + super().get_urls()

    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, id)
        if not self.has_change_permission(request, user):
            raise PermissionDenied
        if user is None:
            msg = _('%(name)s object with primary key %(key)r does not exist.') % {
                'name': self.model._meta.verbose_name,
                'key': id,
            }
            messages.warning(request, msg)
            return HttpResponseRedirect(
                reverse('%s:%s_%s_account_user_changelist' % (
                    self.admin_site.name,
                    'account',
                    'user',
                ))
            )
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = _('Password changed successfully.')
                messages.success(request, msg)
                return HttpResponseRedirect(
                    reverse(
                        '%s:%s_%s_change' % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk, ),
                    )
                )
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % str(user),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
            **self.admin_site.each_context(request),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template or 'admin/auth/user/change_password.html',
            context,
        )


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
    ordering = ('-id', )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    ordering = ('id', )

    def user(self, obj):
        return [_.username for _ in obj.users.all()]
