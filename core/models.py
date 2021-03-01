from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Home(models.Model):
    pass

class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.CharField(max_length=280)
    release_year = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="artists")

    def __str__(self):
        return f"{self.title}, {self.artist}, {self.release_year}"

class Artist(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


