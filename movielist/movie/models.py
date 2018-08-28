from django.db import models
from django.urls import reverse

from movielist.core.models import Audit

# Create your models here.


class Movie(Audit):

    title = models.CharField(max_length=128, unique=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.pk})
