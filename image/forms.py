from django import forms

from image.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file', 'is_public', 'description', ]
        widgets = {
            'image_file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
