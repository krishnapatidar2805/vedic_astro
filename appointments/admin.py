from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'service', 'preferred_date', 'preferred_time', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'consultation_mode', 'service', 'preferred_date')
    search_fields = ('full_name', 'phone', 'email', 'user__username')
    date_hierarchy = 'preferred_date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Client Info', {'fields': ('user', 'full_name', 'phone', 'email')}),
        ('Birth Details', {'fields': ('date_of_birth', 'time_of_birth', 'place_of_birth')}),
        ('Appointment Details', {'fields': ('service', 'preferred_date', 'preferred_time', 'consultation_mode', 'message')}),
        ('Status & Notes', {'fields': ('status', 'admin_notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
