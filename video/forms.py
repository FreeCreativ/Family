from django import forms

from video.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file', 'description', ]
        widgets = {
            'video_file': forms.ClearableFileInput(attrs={'multiple': True}),
        }