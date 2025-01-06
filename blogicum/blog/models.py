from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Добавлено"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
        blank=False
    )

    class Meta:
        abstract = True


class Category(CreateModel):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
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
        verbose_name="Идентификатор",
        help_text=(
            "Идентификатор страницы для URL; "
            "разрешены символы латиницы, цифры, "
            "дефис и подчёркивание."
        ),
        blank=False
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return (
            f"{self.title[:20]} "
            f"(Создано: {self.created_at.strftime('%Y-%m-%d')})")


class Location(CreateModel):
    name = models.CharField(
        max_length=256,
        verbose_name="Название места",
        help_text="Введите название места."
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return (
            f"{self.title[:20]} "
            f"(Создано: {self.created_at.strftime('%Y-%m-%d')})")


class Post(CreateModel):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
        help_text="Введите название публикации.",
        blank=False
    )
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — "
            "можно делать отложенные публикации."
        )
    )
    text = models.TextField(
        verbose_name="Текст",
        help_text="Введите текст публикации.",
        blank=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
        help_text="Выберите автора публикации.",
        blank=False
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Местоположение",
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

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return (
            f"{self.category}, "
            f"Добавлено: {self.created_at.strftime('%Y-%m-%d')})")
