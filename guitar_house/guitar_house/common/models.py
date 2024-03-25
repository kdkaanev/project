from django.contrib.auth import get_user_model
from django.db import models

from guitar_house.guitar.models import Guitar

UserModel = get_user_model()
# Create your models here.



class Message(models.Model):
    sender = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        UserModel, on_delete=models.CASCADE,
        related_name='received_messages'
    )
    guitar = models.ForeignKey(
        Guitar, on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)