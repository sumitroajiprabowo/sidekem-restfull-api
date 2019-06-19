from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_superuser', 'groups')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    list_display = ('email', 'username', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    inlines = (UserProfileInline, )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Province)
admin.site.register(models.Regency)
admin.site.register(models.District)
admin.site.register(models.Village)
