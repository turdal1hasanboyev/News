from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'email',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    search_fields = (
        'name',
        'email',
    )
    fieldsets = (
        ("Contact Create", {'fields': ('name', 'email', 'subject', 'message',)}),
        ("Read only Fields", {'fields': ('created_at', 'updated_at', 'id',)}),
    )
