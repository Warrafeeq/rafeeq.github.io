from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'journal', 'selected']
    list_filter = ['year', 'selected']
    search_fields = ['title', 'authors', 'abstract']