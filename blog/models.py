from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=200, blank=True)
    categories = models.CharField(max_length=200, blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title