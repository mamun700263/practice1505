from django.db import models
from musician.models import Musician
import datetime
# Create your models here.

ratings=[
    ('1','*'),
    ('2',"**"),
    ('3','***'),
    ('4','****'),
    ('5','*****'),
]

class Album(models.Model):
    Album_name = models.CharField(max_length=100)
    Album_musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    Album_release_date = models.DateField()
    Album_Rating = models.CharField(max_length=5,choices=ratings,error_messages='You have to put a rating must')

    def __str__(self):
        return self.Album_name
    
