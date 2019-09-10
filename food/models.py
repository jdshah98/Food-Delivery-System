from django.db import models, connection
from PIL import Image
from django.utils import timezone
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
    id=models.AutoField(primary_key=True,default=0)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    cost = models.CharField(max_length=10)
    image = models.ImageField(default='default.jpg', upload_to='food_pics/')
    date_posted = models.DateTimeField(default=timezone.now)
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rest-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (400, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))
