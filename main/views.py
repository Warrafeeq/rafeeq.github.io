from django.shortcuts import render
from .models import Profile, Education, Experience, Award, News
from publications.models import Publication
from projects.models import Project
from blog.models import Post

def home(request):
    profile = Profile.objects.first()
    selected_publications = Publication.objects.filter(selected=True)[:3]
    recent_news = News.objects.order_by('-date')[:5]
    recent_posts = Post.objects.order_by('-date')[:3]
    
    context = {
        'profile': profile,
        'selected_publications': selected_publications,
        'recent_news': recent_news,
        'recent_posts': recent_posts,
    }
    return render(request, 'main/home.html', context)

def cv(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Award.objects.all()
    
    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'awards': awards,
    }
    return render(request, 'main/cv.html', context)

def about(request):
    profile = Profile.objects.first()
    return render(request, 'main/about.html', {'profile': profile})