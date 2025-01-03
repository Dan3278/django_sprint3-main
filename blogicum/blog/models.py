from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Тематическая категория",
        help_text="Введите название категории.",
        blank=False
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории.",
        blank=False
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг категории",
        help_text="Введите уникальный слаг для категории.",
        blank=False
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Опубликовать ли эту категорию?",
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Тематическая категория"
        verbose_name_plural = "Тематические категории"

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Географическая метка",
        help_text="Введите название географической метки.",
        blank=False
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Опубликовать ли эту локацию?",
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Географическая метка"
        verbose_name_plural = "Географическме метки"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Название публикации",
        help_text="Введите название публикации.",
        blank=False
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(
        verbose_name="Текст публикации",
        help_text="Введите текст публикации.",
        blank=False
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        help_text="Выберите автора публикации.",
        blank=False
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Локация",
        help_text="Выберите локацию для публикации."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        help_text="Выберите категорию публикации.",
        blank=False
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Опубликовать ли эту публикацию?",
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        blank=False
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
