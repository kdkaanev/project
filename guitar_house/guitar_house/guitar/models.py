from django.contrib.auth import get_user_model
from django.db import models



UserModel = get_user_model()
# Create your models here.
CHOICES = (
    ('Acoustic', 'Acoustic'),
    ('Electric', 'Electric'),
    ('Bass', 'Bass'),
    ('Semi-Hollow', 'Semi-Hollow'),
    ('Hollow Body', 'Hollow'),
    ('Other', 'Other')
)
RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
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
        blank=True
    )
    short_description = models.TextField(
        max_length=24,
        blank=True,
        null=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

class Review(models.Model):


    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=1,

    )
    guitar = models.ForeignKey(
        to=Guitar,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

