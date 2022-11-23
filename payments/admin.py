from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_display_price", "description")
    list_display_links = ("id", "name")
