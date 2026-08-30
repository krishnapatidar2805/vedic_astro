from django.contrib import admin
from .models import FAQ, ContactMessage, SiteBanner

admin.site.site_header = "Vedic Gajendra Sharma - Admin Dashboard"
admin.site.site_title = "Vedic Gajendra Sharma Admin"
admin.site.index_title = "Manage Your Astrology Website"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('question', 'answer')
    list_filter = ('is_active',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
