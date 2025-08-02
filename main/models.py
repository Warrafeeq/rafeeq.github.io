from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    github_username = models.CharField(max_length=100, blank=True)
    linkedin_username = models.URLField(blank=True)
    orcid_id = models.URLField(blank=True)
    google_scholar_userid = models.URLField(blank=True)
    research_gate_profile = models.URLField(blank=True)
    sciprofiles_url = models.URLField(blank=True)
    medium_url = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.institution}"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.institution}"

class Award(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.year} - {self.title}"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title