from apps.portfolio.models import Categories
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("id", "created_at", "updated_at")


class CategoriesResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
