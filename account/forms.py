from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from account.models import UserAccount, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth']


class AddUserDetailForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ["gender", "dad", "mum"]


class UpdateSuperUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserAccount
        fields = '__all__'


class CreateSuperUserForm(CreateUserForm):
    class Meta(CreateUserForm.Meta):
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'date_of_birth']


class BiographyForm(forms.ModelForm):
    model = UserAccount
    fields = ['biography', ]


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
