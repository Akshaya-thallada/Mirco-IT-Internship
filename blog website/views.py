from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'registration/register.html', {'form': form})
from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost  # or wherever your blog model is

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
