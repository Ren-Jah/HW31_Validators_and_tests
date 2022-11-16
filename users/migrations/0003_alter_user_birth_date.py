# Generated by Django 4.1.2 on 2022-11-16 21:09

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birth_date_alter_user_age_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(validators=[users.validators.check_birth_date]),
        ),
    ]