from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(request, 'blog/detail.html',
                  {'category': category, 'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, posy_id=post_id)
    if (post.pub_date > timezone.now()
            or not post.is_published
            or not post.category.is_published):
        raise Http404("Публикация не найдена.")

    return render(request, 'blog/post_detail.html', {'post': post})
