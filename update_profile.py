import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile, Education, Experience
from publications.models import Publication

def update_profile():
    """Update profile with detailed information"""
    profile, created = Profile.objects.get_or_create(
        first_name="Muhammed",
        defaults={
            'middle_name': 'Rafeeq',
            'last_name': 'War',
            'email': 'muhammed.24csz0017@iitrpr.ac.in',
            'description': '''Muhammed Rafeeq War is a PhD graduate student at the Prestigious Indian Institute of Technology Ropar with a focus on Computer Science and Engineering. His academic journey includes an MTech in Computer Engineering from Central University of Jammu.

With a strong interest in emerging technologies, War's research delves into areas such as distributed computing, fog computing, edge computing, systems scheduling, and federated learning. He has particularly explored the applications of federated learning in 6G technology. His research also addresses the critical issue of cybersecurity, with a focus on developing a federated learning-based security framework for cyber-physical systems.

Before embarking on his PhD, Muhammed Rafeeq War held the position of Assistant Professor at Lovely Professional University for over a year and a half. He also served as a Teaching Assistant at IIT Ropar during his doctoral studies.''',
            'github_username': 'Warrafeeq',
            'linkedin_username': 'https://www.linkedin.com/in/muhammed-rafeeq-war/',
            'orcid_id': 'https://orcid.org/my-orcid?orcid=0009-0006-7758-6136',
            'google_scholar_userid': 'https://scholar.google.com/citations?user=ypzZCO0AAAAJ&hl=en',
            'research_gate_profile': 'https://www.researchgate.net/profile/Muhammed-Rafeeq-War'
        }
    )
    
    # Update existing profile
    profile.description = '''Muhammed Rafeeq War is a PhD graduate student at the Prestigious Indian Institute of Technology Ropar with a focus on Computer Science and Engineering. His academic journey includes an MTech in Computer Engineering from Central University of Jammu.

With a strong interest in emerging technologies, War's research delves into areas such as distributed computing, fog computing, edge computing, systems scheduling, and federated learning. He has particularly explored the applications of federated learning in 6G technology. His research also addresses the critical issue of cybersecurity, with a focus on developing a federated learning-based security framework for cyber-physical systems.

Before embarking on his PhD, Muhammed Rafeeq War held the position of Assistant Professor at Lovely Professional University for over a year and a half. He also served as a Teaching Assistant at IIT Ropar during his doctoral studies.'''
    profile.save()
    print("Profile updated")

def update_education():
    """Update education information"""
    Education.objects.all().delete()
    
    education_data = [
        {
            'title': 'PhD in Computer Science and Engineering',
            'institution': 'Indian Institute of Technology Ropar',
            'year': '2024-Present',
            'description': 'Research focus on distributed computing, fog computing, edge computing, systems scheduling, and federated learning'
        },
        {
            'title': 'MTech in Computer Engineering',
            'institution': 'Central University of Jammu',
            'year': 'Completed',
            'description': 'Specialized in Computer Engineering with focus on emerging technologies'
        }
    ]
    
    for edu in education_data:
        Education.objects.create(**edu)
    print("Education updated")

def update_experience():
    """Update experience information"""
    Experience.objects.all().delete()
    
    experience_data = [
        {
            'title': 'Teaching Assistant',
            'institution': 'Indian Institute of Technology Ropar',
            'year': '2024-Present',
            'description': 'Supporting doctoral studies and research activities'
        },
        {
            'title': 'Assistant Professor',
            'institution': 'Lovely Professional University',
            'year': '2022-2024 (1.5 years)',
            'description': 'Teaching and research in Computer Science and Engineering'
        }
    ]
    
    for exp in experience_data:
        Experience.objects.create(**exp)
    print("Experience updated")

def add_publications():
    """Add research publications"""
    publications_data = [
        {
            'title': 'Review on the Use of Federated Learning Models for the Security of Cyber-Physical Systems',
            'authors': 'MR War, Y Singh, ZA Sheikh, PK Singh',
            'journal': 'Scalable Computing: Practice and Experience',
            'volume': '26',
            'pages': '16-33',
            'year': '2025',
            'abstract': 'This paper reviews the use of federated learning models for enhancing the security of cyber-physical systems.',
            'selected': True
        },
        {
            'title': 'FedSec-CPS: Federated Learning Based Security Framework for Security of Cyber-Physical Systems',
            'authors': 'MR War, Y Singh, ZA Sheikh',
            'journal': 'Procedia Computer Science',
            'volume': '259',
            'pages': '1837-1844',
            'year': '2025',
            'abstract': 'A federated learning-based security framework for cyber-physical systems.',
            'selected': True
        },
        {
            'title': 'Enhancing Performance of Machine Learning Tasks on Edge-Cloud Infrastructures: A Cross-Domain Internet of Things based Framework',
            'authors': 'MR War, et al.',
            'journal': 'Future Generation Computer Systems',
            'year': '2025',
            'abstract': 'Framework for enhancing machine learning performance on edge-cloud infrastructures.',
            'selected': True
        }
    ]
    
    for pub in publications_data:
        Publication.objects.get_or_create(
            title=pub['title'],
            defaults=pub
        )
    print("Publications added")

if __name__ == '__main__':
    print("Updating profile with detailed information...")
    update_profile()
    update_education()
    update_experience()
    add_publications()
    print("Profile update completed!")