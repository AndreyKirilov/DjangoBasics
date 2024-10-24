from django.db import models
from django.core.validators import MinLengthValidator
from Fruitipedia_app.fruits.validators import is_all_letters_validator
from Fruitipedia_app.profiles.models import Profile


class Fruit(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True,
                            validators=[MinLengthValidator(2), is_all_letters_validator],
                            error_messages={'unique': 'This fruit name is already in use! Try a new one.'})
    image_url = models.URLField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    nutrition = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=False, blank=True,
                              related_name='profile_fruits')
