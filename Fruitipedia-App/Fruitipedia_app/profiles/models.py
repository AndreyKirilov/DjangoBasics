from django.db import models
from django.core.validators import MinLengthValidator
from Fruitipedia_app.profiles.validators import letter_validator


class Profile(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False,
                                  validators=[MinLengthValidator(2), letter_validator])
    last_name = models.CharField(max_length=35, null=False, blank=False,
                                 validators=[MinLengthValidator(1), letter_validator])
    email = models.EmailField(max_length=40, null=False, blank=False, unique=True)
    password = models.CharField(max_length=20, help_text='*Password length requirements: 8 to 20 characters',
                                null=False, blank=False, validators=[MinLengthValidator(8)])
    image_url = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=18)
