from django.db import models

# Create your models here.
INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Drums', 'Drums'),
        ('Bass', 'Bass'),
        ('Keyboard', 'Keyboard'),
        ('Vocals', 'Vocals'),
    ]

class Musician(models.Model):
    musician_first_name = models.CharField(max_length=100,help_text='Enter your first name ')
    musician_last_name = models.CharField(max_length=100,help_text='Enter your last name ')
    musician_email = models.EmailField(help_text='Your Email ')
    musician_number = models.CharField(max_length=15)
    musician_instrument = models.CharField(max_length=20,choices=INSTRUMENT_CHOICES)


    def __str__(self):
        return f"{self.musician_first_name} {self.musician_instrument}"
    
