from django.db import models
from django.urls import reverse


class Service(models.Model):
    """Astrology services offered (Janam Kundli, Kundli Matching, Vastu, etc.)"""
    ICON_CHOICES = [
        ('fa-solid fa-moon', 'Moon'),
        ('fa-solid fa-heart', 'Heart'),
        ('fa-solid fa-ring', 'Ring'),
        ('fa-solid fa-briefcase', 'Briefcase'),
        ('fa-solid fa-chart-line', 'Chart'),
        ('fa-solid fa-house', 'House'),
        ('fa-solid fa-hashtag', 'Hashtag'),
        ('fa-solid fa-hand', 'Hand / Palmistry'),
        ('fa-solid fa-fire', 'Fire / Puja'),
        ('fa-solid fa-clock', 'Muhurat'),
        ('fa-solid fa-star', 'Horoscope'),
        ('fa-solid fa-scale-balanced', 'Court Case'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=170)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-solid fa-star')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Consultation fee in INR")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})
