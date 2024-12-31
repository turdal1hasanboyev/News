from django.contrib import admin

from .models import Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin on the admin site"""
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        'id',
    )
    ordering = ('-id',)
    fieldsets = (
        ("Category Create", {'fields': ('name', "id", "created_at", "updated_at",)}),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag admin on the admin site"""
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        'id',
    )
    ordering = ('-id',)
    fieldsets = (
        ("Tag Create", {'fields': ('name',)}),
        ("Read only Fields", {'fields': ('created_at', 'updated_at', 'id',)}),
    )
