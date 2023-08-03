from apps.portfolio.models import Projects
from rest_framework import serializers
from serializers import CategoriesSerializer


class ProjectsSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    class Meta:
        model = Projects
        fields = ("id", "created_at", "updated_at")


class ProjectsResponseSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Projects
        fields = "__all__"
