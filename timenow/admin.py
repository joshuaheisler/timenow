from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from timenow.models import UserExtended, UserContract, UserRepresent
from absence.models import Absence

# Register your models here.
class UserExtendedInline(admin.StackedInline):
    model = UserExtended
    can_delete = False
    verbose_name_plural = 'user_extended'


class UserAdmin(BaseUserAdmin):
    inlines = (UserExtendedInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserContract)
admin.site.register(UserRepresent)
admin.site.register(Absence)