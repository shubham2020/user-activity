from django.contrib import admin
from Member.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("real_world_id", "username", "timeZone")
    
admin.site.register(User, UserAdmin)