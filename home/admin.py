# admin.py
from django.contrib import admin
from .models import Storeinstruments

from django.utils.html import format_html

class StoreinstrumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'created_at', 'display_image']
    list_editable = ['price']
    search_fields = ['title', 'description', 'category']
    list_filter = ['category']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Product Details', {
            'fields': ('price', 'category')
        })
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image"


admin.site.register(Storeinstruments, StoreinstrumentsAdmin)





