import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile

def add_social_links():
    """Add additional social media links"""
    profile = Profile.objects.first()
    if profile:
        profile.sciprofiles_url = 'https://sciprofiles.com/profile/MuhammedRafeeqWar'
        profile.medium_url = 'https://medium.com/@warrafeeq0'
        profile.save()
        print("Social media links added")
    else:
        print("No profile found")

if __name__ == '__main__':
    add_social_links()