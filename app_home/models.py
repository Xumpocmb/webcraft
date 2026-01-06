from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("service_detail", kwargs={"pk": self.pk})


class ContactRequest(models.Model):
    STATUS_CHOICES = [
        ("new", "Новая"),
        ("in_progress", "В обработке"),
        ("completed", "Завершена"),
        ("cancelled", "Отменена"),
    ]
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    message = models.TextField(verbose_name="Сообщение")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new", verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка на обратную связь"
        verbose_name_plural = "Заявки на обратную связь"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заявка от {self.name} ({self.phone_number})"


class Comment(models.Model):
    contact_request = models.ForeignKey(ContactRequest, on_delete=models.CASCADE, related_name="comments", verbose_name="Заявка")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["created_at"]

    def __str__(self):
        return f"Комментарий от {self.author.username} к заявке №{self.contact_request.id}"
