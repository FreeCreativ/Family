from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import UserAccount, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


class UpdateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount
        fields = (
            "alive", "profile_image", "first_name", "middle_name", "last_name", "email", "date_of_birth", "gender",
            "genotype", "dad", "mum", "height", "biography")


class SuperUserForm(UpdateUserForm):
    class Meta(UpdateUserForm.Meta):
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'date_of_birth']


class BiographyForm(forms.ModelForm):
    model = UserAccount
    fields = ['biography', ]


class AddUserDetailForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['date_of_birth', 'gender', 'blood_group', 'genotype', 'profile_image', 'dad']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('user', 'id',)


class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        exclude = ('user', 'id',)


class PhoneRecordForm(forms.ModelForm):
    class Meta:
        model = PhoneRecord
        exclude = ('user',)


class EmailForm(forms.ModelForm):
    class Meta:
        model = AdditionalEmail
        exclude = ('user', 'id',)


class GeneticDiseaseForm(forms.ModelForm):
    class Meta:
        model = GeneticDisease
        exclude = ('user', 'id',)
