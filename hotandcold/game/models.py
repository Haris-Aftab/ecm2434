from django.db import models
from django.contrib.auth.models import User

# Create the user model
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username
