from django.db import models
from django.conf import settings

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participates')
    