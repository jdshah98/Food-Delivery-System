from django.db import models
from PIL import Image
from users.models import User

# Create your models here.
class RestProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	restaurantname = models.CharField(max_length=20, null=True)
	managername = models.CharField(max_length=20, null=True)
	phone = models.CharField(max_length=13, null=True)
	address = models.CharField(max_length=255, null=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)