from django.utils import timezone
from .models import Post


def post_query(category=None):
    queryset = Post.objects.select_related('author', 'location',
                                           'category').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )

    if category:
        queryset = queryset.filter(category=category)

    return queryset
