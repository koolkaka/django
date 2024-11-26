from django.db import models
from django.contrib.auth.models import User

class VlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Vlog Title")
    video_url = models.URLField(max_length=500, verbose_name="Video URL")
    description = models.TextField(verbose_name="Description")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Published Date")
    tags = models.CharField(max_length=200, verbose_name="Tags")

    def __str__(self):
        return self.title