from django.contrib import admin
from django.db import models
from .models import Category, Post, Location

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)


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

    formfield_overrides = {
        models.BooleanField: {
            'help_text': ('Снимите галочку, чтобы скрыть публикацию.')
        },
        models.SlugField: {
            'help_text': (
                'Идентификатор страницы для URL; разрешены символы '
                'латиницы, цифры, дефис и подчёркивание.'
            )
        },
    }


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)

    formfield_overrides = {
        models.BooleanField: {
            'help_text': ('Снимите галочку, чтобы скрыть публикацию.')
        },
    }


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'created_at'
                    )
    list_filter = ('is_published', 'author', 'category', 'location')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': (
                'title', 'text', 'pub_date', 'author',
                'category', 'location', 'is_published'
            )
        }),
    )
    formfield_overrides = {
        models.BooleanField: {
            'help_text': ('Снимите галочку, чтобы скрыть публикацию.')
        },
        models.SlugField: {
            'help_text': (
                'Идентификатор страницы для URL; разрешены символы '
                'латиницы, цифры, дефис и подчёркивание.'
            )
        },
        models.DateTimeField: {
            'help_text': (
                'Если установить дату и время в будущем — можно делать '
                'отложенные публикации.'
            )
        },
    }
