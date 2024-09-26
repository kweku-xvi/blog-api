from .models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_verified')
    readonly_fields = ('created_at',)


admin.site.register(User, UserAdmin)
