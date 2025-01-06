from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post, Category
from .queries import post_query


def index(request):
    posts = post_query()[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    posts = post_query(category=category)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id, pub_date__lte=timezone.now(),
                             is_published=True, category__is_published=True)
    template: str = 'blog/detail.html'
    if post.pub_date > timezone.now(
    ) or not post.is_published or not post.category.is_published:
        raise Http404('Публикация не найдена')

    return render(request, template, {'post': post})
