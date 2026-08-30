from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    MODE_CHOICES = [
        ('phone', 'Phone Call'),
        ('whatsapp', 'WhatsApp Video Call'),
        ('in_person', 'In-Person Visit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='appointments')
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    time_of_birth = models.TimeField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=150, blank=True)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    consultation_mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='phone')
    message = models.TextField(blank=True, help_text="Briefly describe your problem/question")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.service} ({self.preferred_date})"
