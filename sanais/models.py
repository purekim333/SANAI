from django.db import models

# Create your models here.
class Popular(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    