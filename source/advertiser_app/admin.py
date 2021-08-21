from django.contrib import admin
from advertiser_app.models import (
    Advert,
    Status,
    Category
)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'status']
    list_filter = ['author', 'title']
    search_fields = ['author', 'title']
    fields = ['id', 'author', 'title', 'description', 'image',
              'price', 'status', 'category', 'is_deleted', 'created_at', 'updated_at', 'published_at']
    readonly_fields = ['id', 'created_at', 'updated_at', 'published_at']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['id', 'status']
    readonly_fields = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['id', 'category']
    readonly_fields = ['id']
