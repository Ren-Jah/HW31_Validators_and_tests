from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


def check_birth_date(birth_date):
    diff = relativedelta(date.today(), birth_date).years
    if diff < 9:
        raise ValidationError(f"Запрещена регистрация пользователям младше 9 лет.")

