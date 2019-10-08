from django.db import models

class ImageModel(models.Model):
    image_name = models.CharField(max_length=1000)
    image_date = models.DateTimeField()
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.image_name


class ImageDerivModel(models.Model):
    image_deriv_fk = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=1000)
    image_date = models.DateTimeField()
    image_url = models.CharField(max_length=1000)
    deriv_type = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name
