from django.shortcuts import render
from .models import Profile, Category, Post

# Create your views here.
def index(request):
    # items = Post.objects.filter(status='published')[:10]
    items = Post.published.all()[:10]
    return render(request, 'index.html', {'items': items})

def details(request, pid):
    item = Post.objects.get(id=pid)
    tags = item.tags.split(',')

    # prev
    try:
        prev_post = item.get_previous_by_created()
    except Post.DoesNotExist:
        prev_post = None
    # next
    try:
        next_post = item.get_next_by_created()
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


def posts(request):
    """ 博文日誌列表 """
    # items = Post.objects.filter(status='published')[:10]
    items = Post.published.all()[:10]
    categories = Category.objects.all()    
    return render(request, 'post-list.html', {'items': items, 'categories': categories})