from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('fun', 'Fun'),
        ('research', 'Research'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    importance = models.IntegerField(default=1)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='work')
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['importance']
    
    def __str__(self):
        return self.title