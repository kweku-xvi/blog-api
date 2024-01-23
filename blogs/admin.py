from .models import Blog
from django.contrib import admin


class BlogAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title', 'author', 'date_published')
    readonly_fields = ('date_published', 'time_published')


admin.site.register(Blog, BlogAdmin)
