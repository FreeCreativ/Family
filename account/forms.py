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
        fields = ['date_of_birth', 'gender', 'blood_group', 'genotype', 'image', 'parent']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('user',)


class OccupationForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Occupation


class PhoneRecordForm(forms.ModelForm):
    class Meta:
        fields = ('phone_number',)
        model = PhoneRecord


class EmailForm(forms.ModelForm):
    class Meta:
        fields = ('email',)
        model = AdditionalEmail


class GeneticDiseaseForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = GeneticDisease
