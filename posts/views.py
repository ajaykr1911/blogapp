from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    allposts = Post.objects.all()
    return render(request, 'home.html', {'pts': allposts})
# pts is a list of dictionaries

def post(request, pk):
    pt = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'pt':pt})
#pt is a dictionary