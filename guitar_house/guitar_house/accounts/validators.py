from django.core.exceptions import ValidationError


def validate_phone_number(phone_number):
    if not phone_number.isnumeric():
        raise ValidationError("Phone number should only contain numbers")
