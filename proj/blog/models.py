from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

    
class Post(models.Model):

    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Tag(models.Model):
    name=models.CharField(max_length=50)
    post=models.ManyToManyField(Post)
    def __str__(self):
        return self.name