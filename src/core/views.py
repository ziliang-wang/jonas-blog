from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Profile, Category, Post, Comment
from taggit.models import Tag
from django.urls import reverse
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # items = Post.objects.filter(status='published')[:10]
    items = Post.published.all()[:10]
    return render(request, 'index.html', {'items': items})


def details(request, slug):

    # item = Post.objects.get(id=pid)
    item = Post.objects.get(slug=slug)
    # tags = item.tags.split(',')
    item.views += 1
    item.save()
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

    if request.method == 'POST':
        name = request.POST.get('name', None)
        body = request.POST.get('body', None)

        if name and body:
            comment = Comment()
            comment.post = item
            comment.name = name
            comment.body = body
            comment.ip = get_client_ip(request)
            comment.save()  

        return redirect(item.get_absolute_url())

    return render(request, 'details.html', 
                  {'item': item, 
                #    'tags': tags, 
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
    # items = Post.published.all()[:10]
    items = Post.published.all()
    # 按 標簽 / 分類 過濾
    tag = request.GET.get('tag', None)
    cat = request.GET.get('cat', None)

    if tag:
        tag_obj = Tag.objects.get(slug=tag)
        items = items.filter(tags__in=[tag_obj])
    
    if cat:
        items = items.filter(category__id=cat)

    # 分頁器
    paginator = Paginator(items, 10)
    # 頁碼
    page = request.GET.get('page')
    # pager對像
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    categories = Category.objects.all()    
    return render(request, 'post-list.html', {'items': items, 'categories': categories})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def search_posts(request):

    items = Post.published.all()

    q = request.GET.get('q', None)

    if q.strip():
        items = items.filter(title__contains=q)
    else:
        return redirect(reverse('posts'))

    paginator = Paginator(items, 10)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post-search.html', {
        'page': page,
        'items': posts
    })