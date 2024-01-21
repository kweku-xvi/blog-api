from .models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(User, UserAdmin)
