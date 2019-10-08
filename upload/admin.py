from django.contrib import admin

from .models import ImageModel, ImageDerivModel

# Register your models here.
admin.site.register(ImageModel)
admin.site.register(ImageDerivModel)
