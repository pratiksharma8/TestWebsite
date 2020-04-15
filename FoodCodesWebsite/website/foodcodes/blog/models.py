from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos', blank=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
