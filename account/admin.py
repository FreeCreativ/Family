from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.forms import CreateSuperUserForm, UpdateSuperUserForm
from account.models import UserAccount, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    form = UpdateSuperUserForm
    add_form = CreateSuperUserForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {
            "fields": (
                "alive", "profile_image", "first_name", "middle_name", "last_name", "email", "date_of_birth",
                "gender", "blood_group", "genotype", "dad", "mum", "height", "biography"
            )}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),)


admin.site.register(UserAccount, CustomUserAdmin)
admin.site.register(Education)
admin.site.register(Occupation)
admin.site.register(PhoneRecord)
admin.site.register(AdditionalEmail)
admin.site.register(GeneticDisease)
