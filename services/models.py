import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    """Astrology services offered (Janam Kundli, Kundli Matching, Vastu, etc.)"""
    ICON_CHOICES = [
        ('fa-solid fa-om', 'Om / Divine'),
        ('fa-solid fa-star', 'Horoscope / Nakshatra'),
        ('fa-solid fa-moon', 'Moon / Chandra'),
        ('fa-solid fa-sun', 'Sun / Surya'),
        ('fa-solid fa-fire', 'Fire / Havan / Puja'),
        ('fa-solid fa-ring', 'Ring / Vivah / Marriage'),
        ('fa-solid fa-heart', 'Heart / Love / Relation'),
        ('fa-solid fa-gem', 'Gemstone / Ratna'),
        ('fa-solid fa-house', 'House / Vastu'),
        ('fa-solid fa-briefcase', 'Briefcase / Career / Job'),
        ('fa-solid fa-chart-line', 'Chart / Business / Vyapar'),
        ('fa-solid fa-hand', 'Hand / Palmistry / Hastrekha'),
        ('fa-solid fa-clock', 'Clock / Shubh Muhurat'),
        ('fa-solid fa-scale-balanced', 'Scale / Court Case / Dispute'),
        ('fa-solid fa-feather', 'Feather / Bhagwat Katha'),
        ('fa-solid fa-shield-halved', 'Shield / Suraksha Kavach'),
        ('fa-solid fa-bell', 'Temple Bell / Mandir Ghanti'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=170, blank=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-solid fa-star')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Consultation fee in INR")
    is_featured = models.BooleanField(default=False, verbose_name="Featured Service", help_text="Check to display this service prominently in the Featured section on Homepage")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            candidate = slugify(self.title)
            if not candidate:
                candidate = f"service-{uuid.uuid4().hex[:6]}"
            base_slug = candidate
            counter = 1
            while Service.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base_slug}-{counter}"
                counter += 1
            self.slug = candidate
        super().save(*args, **kwargs)

