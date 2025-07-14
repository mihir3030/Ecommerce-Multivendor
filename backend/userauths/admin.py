from django.contrib import admin
from .models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user_email', 'gender', 'country']
    # list_editable = ['gender']  # in line edit dont look good
    search_fields = ['full_name']
    list_filter = ['date'] 

    def user_email(self, obj):
        return obj.user.email
    
    user_email.short_description = "User Email"

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)