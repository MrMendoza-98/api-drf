from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from profiles_api import models
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None,
            {
                'fields': ('email', 'password')
            }
        ),
        (_('Personal Info'),
            {
                'fields': ('name', )
            }
        ),
        (_('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('Important Dates'),
            {
                'fields': ('last_login', )
            }
        )
    )
    add_fieldsets = (
        (None,
            {
                'classes': ('wide', ),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

# Register your models here.
admin.site.register(models.UserProfile, UserAdmin)
admin.site.register(models.ProfileFeedItem)