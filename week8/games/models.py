from django.db import models

class VideoGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title
