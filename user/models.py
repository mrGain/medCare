from django.db import models
from pkg_resources import require

# Create your models here.

class userModel(models.Model):
    """Model definition for userModel."""

    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.email
