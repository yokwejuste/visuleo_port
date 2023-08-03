from apps.portfolio.models import Skills
from rest_framework import serializers


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ("id", "created_at", "updated_at")


class SkillsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"
