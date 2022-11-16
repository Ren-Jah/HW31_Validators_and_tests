from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.validators import check_birth_date


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местеположение'
        verbose_name_plural = 'Местеположения'

    def __str__(self):
        return self.name


class UserRole:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (MODERATOR, 'Модератор'),
               (ADMIN, 'Администратор'))


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default=UserRole.MEMBER, max_length=20)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(verbose_name="email address", blank=True, validators=[RegexValidator(
        regex="@rambler.ru", inverse_match=True,
        message="Регистрация с данного домена запрещена.")])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        #self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} {self.role}"
