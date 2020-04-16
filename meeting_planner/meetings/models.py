from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=100)
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    # looking up how to do a picklist for the choices
    floor_num_choices = [
        ('FIRST', '1st'),
        ('SECOND', '2nd'),
        ('THIRD', '3rd'),
        ('FOURTH', '4th'),
        ('FIFTH', '5th'),
    ]
    floor_num = models.CharField(
        max_length=6,
        choices=floor_num_choices,
        default='FIRST',
    )
    room_num = models.IntegerField()

    def __str__(self):
        return f'{self.room_name}: room {self.room_num} on floor {self.floor_num}'

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} at {self.start_time} on {self.date}'