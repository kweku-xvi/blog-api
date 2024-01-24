import uuid
from accounts.models import User
from blogs.models import Blog
from django.db import models


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-created_at',)
