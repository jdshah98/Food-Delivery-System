from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Food(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    cost = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
