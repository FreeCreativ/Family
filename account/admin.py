from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.forms import SuperUserForm
from account.models import UserAccount, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    add_form = SuperUserForm


admin.site.register(UserAccount, CustomUserAdmin)
admin.site.register(Education)
admin.site.register(Occupation)
admin.site.register(PhoneRecord)
admin.site.register(AdditionalEmail)
admin.site.register(GeneticDisease)
