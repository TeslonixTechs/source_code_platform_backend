from django.db import models
from django.conf import settings
from repositories.models import Repository

# Create your models here.

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    repository = models.ForeignKey(Repository, related_name='issues', on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issues', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='open')

    def __str__(self):
        return self.title