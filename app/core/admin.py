from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext as _
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    readonly_fields = ('date_joined', 'last_login')

    list_display = [
        'id',
        'email',
        'first_name',
        'last_name',
        'date_joined',
    ]

    fieldsets = (
        (
            _('Login Info'), {
                'fields': (
                    'email',
                    'password',
                )
            }
        ),
        (
            _('Personal Info'), {
                'fields': (
                    'first_name',
                    'last_name',
                )
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Date Infos'), {
                'fields': (
                    'date_joined',
                    'last_login',
                )
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
