from django.db import models

# from base.views import room
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic a user is learning about."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # SET_DEFAULT
    body = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
