from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    author = models.CharField(max_length=100, verbose_name="Автор")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Оценка")
    comment = models.TextField(verbose_name="Комментарий")
    likes = models.PositiveIntegerField(default=0, verbose_name="Лайки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв от {self.author}"

class Reply(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies', verbose_name="Отзыв")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Ответ на отзыв"
        verbose_name_plural = "Ответы на отзывы"
        ordering = ['created_at']

    def __str__(self):
        return f"Ответ от {self.author.username} на отзыв №{self.review.id}"