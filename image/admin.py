from django.contrib import admin

# Register your models here.
from image.models import Image, ImageComment

admin.site.register(Image)
admin.site.register(ImageComment)
