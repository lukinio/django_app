from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
