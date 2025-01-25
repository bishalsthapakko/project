# from django.contrib import admin
# # admin.py
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Storeinstruments

# class StoreinstrumentsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'image_preview','created_at']
#     search_fields = ['title', 'description']
    
#     def image_preview(self, obj):
#         return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    
#     image_preview.short_description = 'Image Preview'

# admin.site.register(Storeinstruments, StoreinstrumentsAdmin)


# Register your models here.

from django.contrib import admin
from django.utils.html import format_html
from .models import Storeinstruments

class StoreinstrumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'price', 'category', 'created_at']
    list_filter = ['category']  # Add filter by category
    search_fields = ['title', 'description', 'category']
    list_editable = ['price']  # Allow price editing directly from list view
    
    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    
    image_preview.short_description = 'Image Preview'

    # Optional: Add fieldsets for better organization in the admin form
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Product Details', {
            'fields': ('price', 'category')
        })
    )

admin.site.register(Storeinstruments, StoreinstrumentsAdmin)

