from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_featured', 'is_active', 'order', 'created_at')
    list_editable = ('price', 'is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active', 'created_at')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'icon', 'price'),
            'description': 'Enter the service title, dakshina/fee, and pick an auspicious Vedic icon.'
        }),
        ('Descriptions & Media', {
            'fields': ('short_description', 'description', 'image'),
            'description': 'Short description is shown on cards; full description is shown on the detail page.'
        }),
        ('Featured & Display Settings', {
            'fields': ('is_featured', 'is_active', 'order'),
            'description': 'Check "Featured Service" to highlight this service on the Homepage.'
        }),
    )

