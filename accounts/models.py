from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Simple Profile model to test app registration and migrations.
    If you already use a custom user model, adapt the USER_MODEL reference.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile for {self.user}"