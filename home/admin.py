# admin.py
from django.contrib import admin
from .models import Storeinstruments

class StoreinstrumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'created_at']
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

admin.site.register(Storeinstruments, StoreinstrumentsAdmin)
