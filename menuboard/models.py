# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Board(models.Model):
    type = models.CharField(max_length=255)
    date_creation = models.DateTimeField()

    class Meta:
        db_table = 'board'
		
class Instruction(models.Model):
    texte = models.CharField(max_length=500, blank=True, null=True)
    ordre = models.IntegerField(default=1)

    class Meta:
        db_table = 'instruction'

class Ingredient(models.Model):
    nom = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    class_color = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'ingredient'
		
class Cocktail(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    taste = models.CharField(max_length=500, blank=True, null=True)
    glass = models.CharField(max_length=500, blank=True, null=True)
    blend = models.CharField(max_length=500, blank=True, null=True)
    alcohol = models.IntegerField(default=0)
    sweetness = models.IntegerField(default=0)
    bitterness = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredient')
    instructions = models.ManyToManyField(Instruction)

    class Meta:
        db_table = 'cocktail'

class CocktailIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite_nombre = models.CharField(max_length=500, blank=True, null=True)
    quantite_type = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'cocktail_ingredient'
