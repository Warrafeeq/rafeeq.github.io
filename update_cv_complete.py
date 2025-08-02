import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile, Education, Experience, Award
from publications.models import Publication

def update_complete_profile():
    """Update profile with complete CV information"""
    profile = Profile.objects.first()
    if profile:
        profile.email = 'warrafeeq0@gmail.com'
        profile.description = '''Dedicated and innovative Computer Science expert with MTech in Artificial Intelligence, seeking an Assistant Professor position in CSE. Combining core CSE subjects, web development, software engineering, and machine learning expertise to advance research and education in secure cyber-physical systems.

Muhammed Rafeeq War is a PhD graduate student at the Prestigious Indian Institute of Technology Ropar with a focus on Computer Science and Engineering. His academic journey includes an MTech in Computer Engineering from Central University of Jammu.

With a strong interest in emerging technologies, War's research delves into areas such as distributed computing, fog computing, edge computing, systems scheduling, and federated learning. He has particularly explored the applications of federated learning in 6G technology.'''
        profile.save()
    print("Profile updated")

def update_education_complete():
    """Update complete education information"""
    Education.objects.all().delete()
    
    education_data = [
        {
            'title': 'PhD in Computer Science and Engineering',
            'institution': 'Indian Institute of Technology Ropar',
            'year': '2024-Present',
            'description': 'Research focus on distributed computing, fog computing, edge computing, systems scheduling, and federated learning'
        },
        {
            'title': 'MTech Computer Science and Technology',
            'institution': 'Central University of Jammu, Jammu, India',
            'year': 'Oct 2021 - May 2023',
            'description': 'Specialized in Artificial Intelligence and Computer Science Technology'
        },
        {
            'title': 'BTech Computer Science and Engineering',
            'institution': 'Pacific University, Udaipur, India',
            'year': 'July 2017 - Aug 2021',
            'description': 'Recipient of Prime Ministers Special Scholarship Scheme'
        }
    ]
    
    for edu in education_data:
        Education.objects.create(**edu)
    print("Education updated")

def update_experience_complete():
    """Update complete experience information"""
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
            'year': 'July 2023 - December 2024',
            'description': 'Teaching Web development with MERN and Mean stack, Networking and Cybersecurity, Pentesting and Data Structures and Algorithms'
        },
        {
            'title': 'Head Developer, Advisor and Architect',
            'institution': 'Quickart.com',
            'year': '2022-2023',
            'description': 'Upcoming ecommerce startup having funding from major tech giants'
        },
        {
            'title': 'Network and Cybersecurity Engineer',
            'institution': 'Freelancing',
            'year': '2021-2023',
            'description': 'Bug hunter and cybersecurity consultant'
        },
        {
            'title': 'Mathematics Teacher',
            'institution': 'Shah Aman Memorial School, Baramulla',
            'year': 'January 2017 - July 2017',
            'description': 'Teaching mathematics to middle school students'
        }
    ]
    
    for exp in experience_data:
        Experience.objects.create(**exp)
    print("Experience updated")

def add_complete_publications():
    """Add all publications and patents"""
    Publication.objects.all().delete()
    
    publications_data = [
        {
            'title': 'Review on the use of Federated Learning (FL) Models for the Security of Cyber-Physical Systems (CPS)',
            'authors': 'Muhammed Rafeeq War, Y Singh, ZA Sheikh, PK Singh',
            'journal': 'Scalable Computing: Practice and Experience (SCPE)',
            'year': '2023',
            'abstract': 'Comprehensive review on federated learning applications in cyber-physical systems security.',
            'selected': True
        },
        {
            'title': 'FedSec-CPS: Federated Learning Based Security Framework for Security of Cyber-Physical Systems',
            'authors': 'Muhammed Rafeeq War, Y Singh, ZA Sheikh',
            'journal': 'Springer',
            'year': '2023',
            'abstract': 'Methodology to improve computational efficiency and security of CPS using horizontal and vertical federated learning.',
            'selected': True
        },
        {
            'title': 'Threats and Risks in Modern Digital HealthCare',
            'authors': 'Muhammed Rafeeq War, et al.',
            'journal': 'Elsevier (Book Chapter)',
            'year': '2023',
            'abstract': 'Analysis of security threats in digital healthcare systems.',
            'selected': False
        },
        {
            'title': 'Social Engineering in Pentesting',
            'authors': 'Muhammed Rafeeq War, et al.',
            'journal': 'Elsevier (Book Chapter)',
            'year': '2023',
            'abstract': 'Comprehensive guide to social engineering techniques in penetration testing.',
            'selected': False
        },
        {
            'title': 'Robotic Systems in Internet of Things: Addressing Security Challenges through Threat Modeling and Penetration Testing',
            'authors': 'Muhammed Rafeeq War, et al.',
            'journal': 'International Journal of Intelligent Robotics and Applications',
            'year': '2023',
            'abstract': 'Security analysis of robotic systems in IoT environments.',
            'selected': True
        },
        {
            'title': 'Secure Penetration Testing and Blockchain Systems Using Federated Learning for Enhanced Privacy',
            'authors': 'Muhammed Rafeeq War, et al.',
            'journal': 'IP India Patent',
            'year': '2024',
            'abstract': 'Patent for secure penetration testing using federated learning.',
            'selected': False
        }
    ]
    
    for pub in publications_data:
        Publication.objects.create(**pub)
    print("Publications and patents added")

if __name__ == '__main__':
    print("Updating complete CV information...")
    update_complete_profile()
    update_education_complete()
    update_experience_complete()
    add_complete_publications()
    print("Complete CV update finished!")