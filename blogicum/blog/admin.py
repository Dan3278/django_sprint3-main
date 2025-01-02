from django.contrib import admin
from .models import Post, Category, Location


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug', 'is_published')
        }),
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date',
                    'is_published', 'created_at')
    list_filter = ('is_published', 'author',
                   'category', 'location')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'pub_date',
                       'author', 'category', 'location',
                       'is_published')
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
