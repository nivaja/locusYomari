from django.db import models

# Create your models here.

class Room(models.Model):
	name= models.CharField(max_length=20)

class Chat(models.Model):
	uid = models.IntegerField()
	chat = models.CharField(max_length=5000)
	roomid = models.IntegerField()
