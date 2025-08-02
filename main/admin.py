from django.contrib import admin
from .models import Profile, Education, Experience, Award, News

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution', 'year']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution', 'year']

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['year', 'title']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']