from django.db import models
from PIL import Image
from users.models import User
from django.urls import reverse

# Create your models here.


class Feedback(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return "Feedback : " + self.username


class Food(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=30,null=True)
    cost = models.CharField(max_length=10,null=True)
    image = models.ImageField(default='default.jpg', upload_to='food_pics')
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "done"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('food-detail', kwargs={'pk': self.pk})
