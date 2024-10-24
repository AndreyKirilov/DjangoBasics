from django.core.exceptions import ValidationError


def letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')
