from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):

    class Meta:
        ordering = ['-date_posted']

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
