from django.db import models

from movielist.core.models import Audit

# Create your models here.


class Movie(Audit):

    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title
