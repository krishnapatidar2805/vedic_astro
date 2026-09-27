from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryImage, GalleryCategory


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'category', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_per_page = 25

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; max-width: 80px; border-radius: 6px; object-fit: cover; box-shadow: 0 1px 4px rgba(0,0,0,0.2);" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"
