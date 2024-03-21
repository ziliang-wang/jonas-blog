from django.shortcuts import render
from .models import Profile, Category, Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request, pid):
    item = Post.objects.get(id=pid)
    tags = item.tags.split(',')
    return render(request, 'details.html', {'item': item, 'tags': tags})

def about(request):
    item = Profile.objects.get(id=1)
    item.hits += 1
    item.save()
    return render(request, 'about.html', {'item': item})