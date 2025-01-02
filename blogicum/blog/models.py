from django.db import models
from django.contrib.auth import get_user_model

User  = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Location(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name="Название")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField(verbose_name="Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts", verbose_name="Автор")
    location = models.ForeignKey(Location, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="posts", verbose_name="Локация")
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name="posts",
                                 verbose_name="Категория")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
