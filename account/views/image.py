from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from image.models import Image


class GeneralImageView(LoginRequiredMixin, ListView):
    model = Image
