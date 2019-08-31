from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.contrib.auth.models import User

from .models import Member


# helps to add users easier in admin
class MemberInLine(admin.StackedInline):
    model = Member
    can_delete = False


class UserAdmin(UserBaseAdmin):
    inlines = (MemberInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)