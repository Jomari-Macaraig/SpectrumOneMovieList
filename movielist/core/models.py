from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


USER = get_user_model()


class Audit(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserAudit(Audit):

    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    class Meta:
        abstract = True
