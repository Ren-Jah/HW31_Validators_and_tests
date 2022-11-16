# Generated by Django 4.1.2 on 2022-11-14 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_category_slug_alter_ad_description_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
