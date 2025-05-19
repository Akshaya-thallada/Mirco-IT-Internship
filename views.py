from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def create_post(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')
    return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
