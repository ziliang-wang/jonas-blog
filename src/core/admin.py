from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'fullname',
        'title',
        'email',
        'line',
        'weixin',
        'created'
    )
    ordering = ('-created',)

admin.site.register(Profile, ProfileAdmin)