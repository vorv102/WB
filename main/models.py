from django.db import models
from django.contrib.auth.models import User

class ServiceCategory(models.Model):
    name = models.CharField("Категория", max_length=100)

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name="Категория",
    )
    name = models.CharField("Название услуги", max_length=200)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена, ₽", max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField("Длительность, мин", default=60)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.price} ₽)"


class Master(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=200)
    experience = models.PositiveIntegerField("Опыт, лет", default=1)
    photo = models.ImageField("Фото", upload_to='masters/', blank=True, null=True)
    description = models.TextField("О мастере", blank=True)
    is_active = models.BooleanField("Работает", default=True)

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('done', 'Выполнена'),
        ('cancelled', 'Отменена'),
    ]

    name = models.CharField("Имя клиента", max_length=200)
    phone = models.CharField("Телефон", max_length=30)
    car = models.CharField("Автомобиль", max_length=200)
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Услуга",
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Мастер",
    )
    date = models.DateField("Желаемая дата")
    comment = models.TextField("Комментарий", blank=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.service} — {self.date}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField("Текст отзыва")
    rating = models.PositiveSmallIntegerField("Оценка (1-5)", default=5)
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.rating} звезд"