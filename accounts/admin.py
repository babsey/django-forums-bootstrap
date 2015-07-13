from django.contrib import admin
from .models import Group, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'Associated account', {'fields': ('user',)}),
        (u'Profile information', {'fields': ('public_email', 'web_page', 'notes',)}),
        (u'Forum', {'fields': ('forum_group', 'forum_email_notification',)}),
        (u'Special', {'fields': ('ip_address',)}),
    )
    list_display = ('user', 'public_email', 'post_count')
    ordering = ('-id',)
    search_fields = ('user__username',)
    raw_id_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
