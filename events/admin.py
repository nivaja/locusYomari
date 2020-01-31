from django.contrib import admin
from .models import Event, EventType, Location

# Register your models here.

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Location)