import uuid
from accounts.models import User
from django.db import models


class Blog(models.Model):
    id = models.CharField(max_length=13, primary_key=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    time_published = models.TimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4())[:13]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
