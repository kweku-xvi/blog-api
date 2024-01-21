from .models import Blog
from django.contrib import admin

# Showing auto_now_add fields date_published and time_published in admin panel
class BlogAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title', 'author', 'date_published')
    readonly_fields = ('date_published', 'time_published')


admin.site.register(Blog, BlogAdmin)
