from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "News Admin Panel"
admin.site.site_title = "News Admin Panel"
admin.site.index_title = "News to Niture Control Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'image',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'last_login',
        "date_joined",
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'password',)
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'image',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login',)
        }),
    )

    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )
