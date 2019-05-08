from django.contrib import admin
from xiaomi_users.models import UserPhoneComment

# Register your models here.
class UserMovieCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserPhoneComment, UserMovieCommentAdmin)