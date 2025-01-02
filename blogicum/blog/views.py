from django.shortcuts import render
from django.http import Http404

posts_dict = {post['id']: post for post in posts}


def index(request):
    context = {'posts': posts[::-1]}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = posts_dict.get(post_id)
    if post is None:
        raise Http404('Указан неверный id')
    context = {'post': post, }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    return render(request, 'blog/category.html',
                  {'category_slug': category_slug})
