from django.db import models

# Create your models here.

from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
from django.contrib.auth import models as auth_models

from guitar_house.accounts.managers import GuitarHouseUserManager
from guitar_house.accounts.validators import validate_phone_number


class GuitarHouseUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    EMAIL_ERROR_MESSAGES = {
        "unique": _("A user with that email already exists."),
    }
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages=EMAIL_ERROR_MESSAGES,
    )
    date_joined = models.DateTimeField(
        _("date joined"), default=timezone.now,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = GuitarHouseUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            validate_phone_number
        ],
        null=False,
        blank=False,
    )
    user = models.OneToOneField(
        to=GuitarHouseUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name or self.last_name



