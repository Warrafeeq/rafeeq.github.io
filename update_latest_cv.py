import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile, Education, Experience
from projects.models import Project

def update_profile_latest():
    profile = Profile.objects.first()
    if profile:
        profile.email = 'muhammed.24csz0017@iitrpr.ac.in'
        profile.save()
    print("Profile email updated")

def update_education_latest():
    Education.objects.all().delete()
    
    education_data = [
        {
            'title': 'PhD in Computer Science Engineering',
            'institution': 'Indian Institute of Technology, Ropar',
            'year': '2025-2027',
            'description': 'Pursuing PhD with focus on cybersecurity, federated learning, and cyber-physical systems'
        },
        {
            'title': 'Master of Technology',
            'institution': 'Central University of Jammu, Jammu',
            'year': '2021-2023',
            'description': 'CGPA: 8.86/10.0'
        }
    ]
    
    for edu in education_data:
        Education.objects.create(**edu)
    print("Education updated")

def update_experience_latest():
    Experience.objects.all().delete()
    
    experience_data = [
        {
            'title': 'Teaching Assistant for Cybersecurity Essentials',
            'institution': 'IIT Ropar',
            'year': 'Jan 2025 - Present',
            'description': 'Teach Students Practical Ethical Hacking. Evaluate the progress of students and design the structure of learning'
        },
        {
            'title': 'Senior Manager and Faculty',
            'institution': 'Futurense Technologies, Bengaluru',
            'year': 'Dec 2024 - Jan 2025',
            'description': 'Prepared curriculum for industrial training. Prepared Curriculum for GenAI, DSA with Python and NLP'
        },
        {
            'title': 'Industrial Trainer and Assistant Professor',
            'institution': 'Lovely Professional University, Jalandhar',
            'year': 'July 2023 - Dec 2024',
            'description': 'Trained students with recent industrial and entrepreneurial skills like ML, NLP, GenAI and Data Science. Taught core CSE subjects like DSA, Programming, Networking, Operating Systems'
        }
    ]
    
    for exp in experience_data:
        Experience.objects.create(**exp)
    print("Experience updated")

def update_projects_latest():
    Project.objects.all().delete()
    
    projects_data = [
        {
            'title': 'Federated Learning for the security of cyber-physical systems',
            'description': 'Leverages Federated Learning to enhance CPS security through decentralized, privacy-preserving threat detection',
            'content': '''This project leverages Federated Learning to enhance the security of Cyber-Physical Systems (CPS) by enabling decentralized, privacy-preserving threat detection. It ensures data confidentiality by training models locally on edge devices without sharing raw data.

Using machine learning techniques, the system detects anomalies and cyber threats in CPS networks while improving model accuracy through collaborative learning. The approach strengthens security in critical infrastructures like SCADA, ICS, and IoT without compromising sensitive information.''',
            'category': 'research',
            'importance': 1,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': 'Fake News Detection Using LSTM',
            'description': 'LSTM with NLP and machine learning to classify fake news articles based on textual features',
            'content': '''This project uses LSTM with NLP and machine learning with scikit-learn in Python to classify fake news articles based on textual features.

It utilizes the LIAR dataset and trains classifiers like Logistic Regression and Random Forest to detect misinformation with an optimized prediction model.''',
            'category': 'work',
            'importance': 2,
            'github_url': 'https://github.com/Warrafeeq'
        }
    ]
    
    for proj in projects_data:
        Project.objects.create(**proj)
    print("Projects updated")

if __name__ == '__main__':
    print("Updating latest CV information...")
    update_profile_latest()
    update_education_latest()
    update_experience_latest()
    update_projects_latest()
    print("Latest CV update completed!")