from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import PostCreateForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    form = PostCreateForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)
