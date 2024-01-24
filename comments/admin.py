from .models import Comment
from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('id', 'blog', 'user', 'created_at')


admin.site.register(Comment, CommentAdmin)