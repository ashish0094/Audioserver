from django.db import models


class Song(models.Model):
    songId = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank= False)
    upload_time = models.TimeField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Podcast(models.Model):
    podId = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    upload_time = models.TimeField()
    host = models.CharField(max_length=100, blank=False)
    participants = models.ManyToManyField(Participant, null=True, blank=True)

    def __str__(self):
        return self.name

class Audiobook(models.Model):
    audioId = models.PositiveIntegerField(default=0, unique=True)
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    narrator = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    upload_time = models.TimeField()

    def __str__(self):
        return self.title






