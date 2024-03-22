from django.db.models import Count
from .models import *


def post_processor(request):
    
    return {
        # 'CATEGORIES': Category.objects.all(),
        'CATEGORIES': Category.objects.values('id', 'name').annotate(Count('posts')),
        'TAGS': ...,
        'LATEST_POSTS': Post.published.all()[:5],
        'RECOMMEND_POSTS': Post.published.filter(flag=True).all()[:5]
    }
    