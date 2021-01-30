from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, help_text="Enter name of the city")
    country = models.CharField(max_length=50, help_text="Enter country")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
