from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_detail,
         name='category_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
