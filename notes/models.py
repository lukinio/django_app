from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.models import MPTTModel
from topics.models import Topic


class Note(TimeStampedModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={'pk': self.pk})