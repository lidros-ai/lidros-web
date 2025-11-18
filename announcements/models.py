from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title