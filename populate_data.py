import os
import django
from datetime import datetime
from django.utils.text import slugify

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile, Education, Experience, Award, News
from blog.models import Post
from projects.models import Project
from publications.models import Publication

def populate_profile():
    """Create profile from Jekyll config data"""
    profile, created = Profile.objects.get_or_create(
        first_name="Muhammed",
        defaults={
            'middle_name': 'Rafeeq',
            'last_name': 'War',
            'email': 'muhammed.24csz0017@iitrpr.ac.in',
            'description': 'PhD Graduate Student at IIT Ropar specializing in Edge Computing, Federated Learning, and Cybersecurity.',
            'github_username': 'Warrafeeq',
            'linkedin_username': 'https://www.linkedin.com/in/muhammed-rafeeq-war/',
            'orcid_id': 'https://orcid.org/my-orcid?orcid=0009-0006-7758-6136',
            'google_scholar_userid': 'https://scholar.google.com/citations?user=ypzZCO0AAAAJ&hl=en',
            'research_gate_profile': 'https://www.researchgate.net/profile/Muhammed-Rafeeq-War'
        }
    )
    print(f"Profile {'created' if created else 'updated'}")

def populate_education():
    """Create education entries"""
    education_data = [
        {
            'title': 'PhD in Computer Science',
            'institution': 'IIT Ropar',
            'year': '2024-Present',
            'description': 'Specializing in Edge Computing, Federated Learning, and Cybersecurity'
        }
    ]
    
    for edu in education_data:
        Education.objects.get_or_create(
            title=edu['title'],
            institution=edu['institution'],
            defaults=edu
        )
    print("Education data populated")

def populate_experience():
    """Create experience entries"""
    experience_data = [
        {
            'title': 'Research Assistant',
            'institution': 'IIT Ropar',
            'year': '2024-Present',
            'description': 'Working on Edge Computing and Federated Learning research projects'
        }
    ]
    
    for exp in experience_data:
        Experience.objects.get_or_create(
            title=exp['title'],
            institution=exp['institution'],
            defaults=exp
        )
    print("Experience data populated")

def populate_awards():
    """Create award entries"""
    awards_data = [
        {'year': '2024', 'title': 'PhD Fellowship, IIT Ropar'}
    ]
    
    for award in awards_data:
        Award.objects.get_or_create(
            year=award['year'],
            title=award['title']
        )
    print("Awards data populated")

def populate_news():
    """Create news entries"""
    news_data = [
        {
            'title': 'Started PhD at IIT Ropar',
            'content': 'Joined the PhD program at IIT Ropar, focusing on Edge Computing and Federated Learning research.',
            'date': datetime(2024, 1, 1).date()
        }
    ]
    
    for news in news_data:
        News.objects.get_or_create(
            title=news['title'],
            defaults=news
        )
    print("News data populated")

def populate_sample_projects():
    """Create sample projects"""
    projects_data = [
        {
            'title': 'Edge Computing Framework',
            'description': 'A distributed computing framework for edge devices',
            'content': 'This project focuses on developing an efficient framework for edge computing that optimizes resource utilization and reduces latency.',
            'category': 'research',
            'importance': 1
        },
        {
            'title': 'Federated Learning System',
            'description': 'Privacy-preserving machine learning system',
            'content': 'Implementation of a federated learning system that enables collaborative machine learning while preserving data privacy.',
            'category': 'research',
            'importance': 2
        }
    ]
    
    for proj in projects_data:
        Project.objects.get_or_create(
            title=proj['title'],
            defaults=proj
        )
    print("Sample projects populated")

def populate_sample_posts():
    """Create sample blog posts"""
    posts_data = [
        {
            'title': 'Introduction to Edge Computing',
            'content': 'Edge computing brings computation and data storage closer to the location where it is needed, improving response times and saving bandwidth.',
            'description': 'An introduction to edge computing concepts and applications',
            'tags': 'edge-computing, research',
            'categories': 'research'
        },
        {
            'title': 'Federated Learning Fundamentals',
            'content': 'Federated learning is a machine learning technique that trains an algorithm across multiple decentralized edge devices or servers.',
            'description': 'Understanding the basics of federated learning',
            'tags': 'federated-learning, machine-learning',
            'categories': 'research'
        }
    ]
    
    for post_data in posts_data:
        slug = slugify(post_data['title'])
        Post.objects.get_or_create(
            slug=slug,
            defaults={**post_data, 'slug': slug}
        )
    print("Sample blog posts populated")

if __name__ == '__main__':
    print("Populating database with Jekyll data...")
    populate_profile()
    populate_education()
    populate_experience()
    populate_awards()
    populate_news()
    populate_sample_projects()
    populate_sample_posts()
    print("Data population completed!")