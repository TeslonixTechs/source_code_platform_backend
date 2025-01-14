from rest_framework import serializers
from .models import Repository
from .models import Issue

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'creator', 'created_at', 'updated_at', 'status']