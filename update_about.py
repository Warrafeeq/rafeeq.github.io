import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from main.models import Profile

def update_profile():
    profile = Profile.objects.first()
    if profile:
        profile.description = '''I am a scholar and expert in cybersecurity, federated learning, and distributed computing. I am currently pursuing a Doctor of Philosophy (PhD) at the Indian Institute of Technology (IIT) Ropar. My academic and professional journey reflects a strong commitment to exploring and implementing innovative solutions to safeguard cyber-physical systems and optimize performance within complex computing environments.

My pursuit of advanced knowledge is highlighted by my enrollment in the PhD program at IIT Ropar, a testament to my dedication to cutting-edge research in computer science and engineering. I earned a Master of Technology (MTech) degree in Computer Engineering from the Central University of Jammu. My research interests include:

• Federated Learning: A distributed machine learning approach that enables collaborative model training without centralizing sensitive data.
• 6G Technology: Investigating the security and performance implications of the next generation of wireless communication networks.
• Cybersecurity & Cryptography: Exploring advanced techniques to protect data, networks, and systems from malicious attacks.
• Edge Computing: Optimizing computational tasks and data processing at the network's edge for enhanced efficiency and responsiveness.
• Critical Infrastructure & Agriculture: Applying my expertise to fortify vital systems in industries like power grids, transportation, and agricultural technology against cyber threats.

My published works include "Review on the Use of Federated Learning Models for the Security of Cyber-Physical Systems," co-authored with colleagues. This research underscores my commitment to developing robust and efficient cybersecurity methodologies for constrained cyber-physical systems utilizing the power of federated learning.

My dedication extends beyond research to encompass teaching and mentorship. I have served as an Assistant Professor at Lovely Professional University. Currently, I am a Teaching Assistant at IIT Ropar, where I actively contribute to the academic environment and guide students through topics like Cybersecurity and Cryptography Essentials (CS558).

My academic prowess is validated by certifications in specialized areas, including Advanced Learning Algorithms, Machine Learning by Andrew Ng, Foundations of Cybersecurity, Bits and Bytes of CN, Generative AI, Introduction to Cybersecurity Tools & Cyber Attacks, and Supervised Machine Learning: Classification.

I represent a rising force in the field of cybersecurity and distributed systems. My academic rigor, research, and dedication to teaching position me as a valuable contributor to the advancement of secure and efficient computing solutions, particularly within the context of critical infrastructure protection and the evolving landscape of federated learning and 6G technologies.'''
        profile.save()
        print("Profile description updated")

if __name__ == '__main__':
    update_profile()