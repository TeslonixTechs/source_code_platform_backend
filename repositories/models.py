from django.db import models
from django.conf import settings
import random

# Create your models here.

class Repository(models.Model):
    REP_PREFIX = "REP-"
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='repositories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference = models.CharField(max_length=10, unique=True, editable=False) # REP-XXXXXXX 10

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self.generate_unique_reference()

        super().save(*args, **kwargs)

    def generate_unique_reference(self):
        while True:
            random_number = random.randint(1000000, 9999999)
            reference - f"{self.REP_PREFIX}{random_number}"
            if not Repository.objects.filter(reference=reference):
                return reference 

    def __str__(self):
        return self.name