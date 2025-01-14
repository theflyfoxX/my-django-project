from django.db import models
from django.core.validators import *



class Breed(models.Model):
    SIZES = [
        ('TINY', 'Tiny'),
        ('SMALL', 'small'),
        ('MEDUIM', 'meduim'),
        ('LARGE', 'large'),
  ]
    validators=[
            MinValueValidator(1),  
            MaxValueValidator(10)  
        ]
    name = models.CharField(max_length=255, blank=False)
    size = models.CharField(
        max_length=10, 
        choices=SIZES, 
    )  
    friendliness = models.IntegerField(validators)
    trainability = models.IntegerField(validators)
    sheddingamount = models.IntegerField(validators)
    exerciseneeds = models.IntegerField(validators)
  
    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=255, blank=False)
    favoritefood = models.CharField(max_length=255, blank=False)
    favoritetoy = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name
    
    
