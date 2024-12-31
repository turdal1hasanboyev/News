from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'image',
        'author',
        'category',
        'views',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    search_fields = (
        'title',
        'category__name',
        'author__email',
        'author__first_name',
        'author__last_name',
    )
    list_filter = (
        'category__name',
        'author',
    )
    fieldsets = (
        ("Create New Article", {'fields': ('title', 'slug', 'image', 'description', 'author', 'category', 'tags', 'views',)}),
        ("Read only fields", {'fields': ('created_at', 'updated_at', 'id',)}),
    )

admin.site.register(Article, ArticleAdmin)
