from django.contrib import admin

from .models import Sub_Email


@admin.register(Sub_Email)
class Sub_EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sub_email',
        'created_at',
        'updated_at',
    )
    search_fields = ('sub_email',)
    ordering = ('id',)
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    fieldsets = (
        ("Sub Email Create", {'fields': ('sub_email', "id", "created_at", "updated_at",)}),
    )
