from django.db import models

class ImageModel(models.Model):
    image_name = models.CharField(max_length=1000)
    image_date = models.DateTimeField()
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.image_name
