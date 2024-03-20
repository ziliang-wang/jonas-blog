from django.shortcuts import render
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request, pid):
    return render(request, 'details.html')

def about(request):
    item = Profile.objects.get(id=1)
    item.hits += 1
    item.save()
    return render(request, 'about.html', {'item': item})