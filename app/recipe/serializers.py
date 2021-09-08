from django.db import models
from django.db.models import fields
from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSeralizer(serializers.ModelSerializer):
    """Serializer for tags objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)