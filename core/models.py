from django.db import models
from django.contrib.auth.models import User

class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    body_fat_percentage = models.FloatField()
    muscle_mass = models.FloatField()
    # Additional metrics

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()
    snacks = models.TextField()

class WorkoutRoutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercises = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food = models.TextField()
    barcode = models.CharField(max_length=255, null=True, blank=True)

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    workout = models.TextField()
    barcode = models.CharField(max_length=255, null=True, blank=True)
