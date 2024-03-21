from django.shortcuts import render
from .models import Profile, Category, Post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request, pid):
    item = Post.objects.get(id=pid)
    tags = item.tags.split(',')

    # prev
    try:
        prev_post = item.get_next_by_created()
    except Post.DoesNotExist:
        prev_post = None
    # next
    try:
        next_post = item.get_previous_by_created()
    except Post.DoesNotExist:
        next_post = None

    return render(request, 'details.html', 
                  {'item': item, 'tags': tags, 
                    'prev_post': prev_post,
                    'next_post': next_post })

def about(request):
    item = Profile.objects.get(id=1)
    item.hits += 1
    item.save()
    return render(request, 'about.html', {'item': item})