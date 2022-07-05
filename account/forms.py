from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import UserAccount, UserDetail, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name']


class AddUserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['date_of_birth', 'gender', 'blood_group', 'genotype', 'image', 'dad']


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
