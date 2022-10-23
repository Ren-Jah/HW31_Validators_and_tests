from django.db import models


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


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    username = models.CharField(verbose_name='Логин', max_length=200, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=200)
    role = models.CharField(choices=UserRole.choices, default=UserRole.MEMBER, max_length=20)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} {self.role}"
