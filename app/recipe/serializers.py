from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


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


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe objects"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all(),
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tags',
                  'time_minutes', 'price', 'link')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for Recipe Detail objects"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSeralizer(many=True, read_only=True)



