from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    content = models.TextField(blank=True, null=True)
    chat =  models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-id']