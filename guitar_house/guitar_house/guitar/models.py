from django.db import models

# Create your models here.
CHOICES = (
    ('Acoustic', 'Acoustic'),
    ('Electric', 'Electric'),
    ('Bass', 'Bass'),
    ('Semi-Hollow', 'Semi-Hollow'),
    ('Hollow Body', 'Hollow'),
    ('Other', 'Other')
)

class Guitar(models.Model):
    brand = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    model = models.CharField(
        null=True,
        blank=True,
        max_length=100)
    type = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        choices=CHOICES
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
    )
    short_description = models.TextField(
        null=True
    )
