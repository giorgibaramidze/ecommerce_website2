from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account, UserProfile
from django.utils.html import format_html

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    def thubnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thubnail.short_description = "Profile Picture"
    list_display = ('thubnail', 'user', 'city', 'state', 'country')
