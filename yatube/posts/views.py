from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUM_POSTS: int = 10


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,

    }
    return render(request, 'posts/index.html', context)
