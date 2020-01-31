from django.db import models

# Create your models here.
from django.utils import timezone


class Location(models.Model):
    LocationName = models.CharField(max_length=100)
    LocationImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.LocationName

class EventType(models.Model):
    EventType=models.CharField(max_length=100)

    def __str__(self):
        return self.EventType

class Event(models.Model):
    EventTypeDescription = models.ForeignKey(EventType, on_delete= models.CASCADE)
    EventLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    EventDate = models.DateTimeField(default=timezone.now)
    EventDescription = models.TextField()

    def __str__(self):
        return self.EventDescription

