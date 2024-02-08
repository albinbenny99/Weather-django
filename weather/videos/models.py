from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=50)  # YouTube video ID

    def __str__(self):
        return self.title
