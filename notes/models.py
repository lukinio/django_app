from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()