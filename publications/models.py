from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=500)
    journal = models.CharField(max_length=200, blank=True)
    year = models.CharField(max_length=10)
    volume = models.CharField(max_length=20, blank=True)
    pages = models.CharField(max_length=50, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    doi = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='publications/', blank=True)
    abstract = models.TextField(blank=True)
    bibtex = models.TextField(blank=True)
    selected = models.BooleanField(default=False)
    preview_image = models.ImageField(upload_to='publications/previews/', blank=True)
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return self.title