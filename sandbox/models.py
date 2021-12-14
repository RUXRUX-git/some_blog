from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
                                  related_name='received_messages')
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

