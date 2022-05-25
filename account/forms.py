from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import UserAccount, UserDetail, Education, Occupation, PhoneRecord, AdditionalEmail, GeneticDisease


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserAccount
        fields = '__all__'


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'


class OccupationForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Occupation


class PhoneRecordForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = PhoneRecord


class EmailForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = AdditionalEmail


class GeneticDiseaseForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = GeneticDisease
