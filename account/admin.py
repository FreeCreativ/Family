from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.forms import UserRegisterForm
from account.models import UserAccount, UserDetail, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


# Register your models here.
class DetailInline(admin.StackedInline):
    model = UserDetail
    can_delete = False
    verbose_name_plural = 'account'


class UserAdmin(BaseUserAdmin):
    inlines = (DetailInline,)


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm


admin.site.register(UserAccount)
admin.site.unregister(UserAccount)
admin.site.register(UserAccount, CustomUserAdmin)
admin.site.register(UserDetail)
admin.site.register(Education)
admin.site.register(Occupation)
admin.site.register(PhoneRecord)
admin.site.register(AdditionalEmail)
admin.site.register(GeneticDisease)
