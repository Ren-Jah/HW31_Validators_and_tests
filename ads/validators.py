from rest_framework import serializers


def not_published(value):
    if value:
        raise serializers.ValidationError(f"При создании объявления не может быть True.")