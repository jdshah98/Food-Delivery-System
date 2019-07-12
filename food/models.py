from django.db import models

# Create your models here.
class Feedback(models.Model):
    username = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=254, null=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
    	return "Feedback : " + self.username